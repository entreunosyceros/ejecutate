#!/usr/bin/env python3
"""
Gestor visual de paquetes Python para principiantes
Facilita la instalación y gestión de paquetes con pip
"""

import subprocess
import sys
import json
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
try:
    from importlib.metadata import distributions
    METADATA_AVAILABLE = True
except ImportError:
    try:
        from importlib_metadata import distributions
        METADATA_AVAILABLE = True
    except ImportError:
        METADATA_AVAILABLE = False
        distributions = None

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    requests = None
import threading
import time

@dataclass
class PackageInfo:
    """Información de un paquete Python"""
    name: str
    version: str = ""
    description: str = ""
    author: str = ""
    home_page: str = ""
    installed: bool = False
    latest_version: str = ""
    size: str = ""
    dependencies: List[str] = None
    category: str = "📦 General"
    pip_name: str = ""
    builtin: bool = False
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if not self.pip_name:
            self.pip_name = self.name

class PackageManager:
    """Gestor de paquetes Python con interfaz amigable"""
    
    def __init__(self):
        self.popular_packages = self._get_popular_packages()
        self.installed_packages = {}
        self._update_installed_packages()
    
    def _get_popular_packages(self) -> Dict[str, PackageInfo]:
        """Catálogo de paquetes habituales agrupados por uso."""
        catalog = [
            # Web y APIs
            ("requests", "Peticiones HTTP sencillas", "🌐 Web", "Kenneth Reitz", "https://requests.readthedocs.io/"),
            ("httpx", "HTTP moderno con soporte async", "🌐 Web", "", "https://www.python-httpx.org/"),
            ("aiohttp", "Cliente y servidor HTTP asíncrono", "🌐 Web", "", "https://docs.aiohttp.org/"),
            ("beautifulsoup4", "Parsear HTML y XML (web scraping)", "🌐 Web", "Leonard Richardson", "https://www.crummy.com/software/BeautifulSoup/"),
            ("selenium", "Automatizar navegadores web", "🌐 Web", "", "https://selenium-python.readthedocs.io/"),
            ("scrapy", "Framework de scraping a gran escala", "🌐 Web", "", "https://scrapy.org/"),
            ("flask", "Framework web minimalista", "🌐 Web framework", "Armin Ronacher", "https://flask.palletsprojects.com/"),
            ("django", "Framework web completo", "🌐 Web framework", "Django Software Foundation", "https://www.djangoproject.com/"),
            ("fastapi", "APIs REST modernas y rápidas", "🌐 Web framework", "", "https://fastapi.tiangolo.com/"),
            ("uvicorn", "Servidor ASGI (para FastAPI, etc.)", "🌐 Web framework", "", "https://www.uvicorn.org/", "uvicorn[standard]"),
            ("jinja2", "Plantillas HTML para webs", "🌐 Web framework", "", "https://jinja.palletsprojects.com/"),
            ("pandas", "Análisis y tablas de datos", "📊 Datos", "Wes McKinney", "https://pandas.pydata.org/"),
            ("numpy", "Arrays y cálculo numérico", "📊 Datos", "Travis Oliphant", "https://numpy.org/"),
            ("openpyxl", "Leer y escribir Excel (.xlsx)", "📊 Datos", "", "https://openpyxl.readthedocs.io/"),
            ("pyyaml", "Archivos YAML (configuración)", "📊 Datos", "", "https://pyyaml.org/"),
            ("python-dotenv", "Variables de entorno desde archivo .env", "📊 Datos", "", "https://github.com/theskumar/python-dotenv"),
            # Visualización y PDF
            ("matplotlib", "Gráficos y visualizaciones", "📈 Visualización", "John D. Hunter", "https://matplotlib.org/"),
            ("seaborn", "Gráficos estadísticos sobre matplotlib", "📈 Visualización", "", "https://seaborn.pydata.org/"),
            ("plotly", "Gráficos interactivos", "📈 Visualización", "", "https://plotly.com/python/"),
            ("reportlab", "Generar documentos PDF", "📄 PDF", "", "https://www.reportlab.com/"),
            ("markdown", "Convertir Markdown a HTML", "📄 Documentos", "", "https://python-markdown.github.io/"),
            # Ciencia
            ("scipy", "Algoritmos científicos y estadística", "🔬 Ciencia", "", "https://scipy.org/"),
            ("scikit-learn", "Aprendizaje automático (ML)", "🔬 Ciencia", "", "https://scikit-learn.org/"),
            # Imágenes y multimedia
            ("pillow", "Abrir, editar y guardar imágenes", "🖼️ Imágenes", "Alex Clark", "https://pillow.readthedocs.io/"),
            ("opencv-python", "Visión por ordenador y vídeo", "🖼️ Imágenes", "", "https://opencv.org/"),
            # Persistencia: ORM, drivers y clientes de BD
            ("sqlalchemy", "ORM y capa de acceso a bases de datos SQL", "💾 Datos y persistencia", "", "https://www.sqlalchemy.org/"),
            ("pymongo", "Driver/cliente oficial para MongoDB", "💾 Datos y persistencia", "", "https://pymongo.readthedocs.io/"),
            ("psycopg2-binary", "Driver PostgreSQL para Python", "💾 Datos y persistencia", "", "https://www.psycopg.org/"),
            # Interfaz gráfica y terminal
            ("pyside6", "Interfaces gráficas (Qt) — usado por este editor", "🖥️ GUI", "", "https://doc.qt.io/qtforpython/"),
            ("customtkinter", "Tkinter con aspecto moderno", "🖥️ GUI", "", "https://github.com/TomSchimansky/CustomTkinter"),
            ("rich", "Texto enriquecido y tablas en terminal", "🖥️ Terminal / TUI", "", "https://rich.readthedocs.io/"),
            ("textual", "Aplicaciones TUI completas en terminal", "🖥️ Terminal / TUI", "", "https://textual.textualize.io/"),
            ("click", "Crear comandos de consola (CLI)", "🖥️ Terminal / TUI", "", "https://click.palletsprojects.com/"),
            ("typer", "CLIs con type hints (sobre Click)", "🖥️ Terminal / TUI", "", "https://typer.tiangolo.com/"),
            # Juegos
            ("pygame", "Juegos y gráficos 2D", "🎮 Juegos", "Pete Shinners", "https://www.pygame.org/"),
            # Utilidades
            ("tqdm", "Barras de progreso en bucles y descargas", "🔧 Utilidades", "", "https://tqdm.github.io/"),
            ("loguru", "Logging sencillo y legible", "🔧 Utilidades", "", "https://loguru.readthedocs.io/"),
            ("python-dateutil", "Fechas y zonas horarias avanzadas", "🔧 Utilidades", "", "https://dateutil.readthedocs.io/"),
            ("cryptography", "Cifrado y seguridad", "🔒 Seguridad", "", "https://cryptography.io/"),
            ("bcrypt", "Hashes de contraseñas", "🔒 Seguridad", "", "https://github.com/pyca/bcrypt/"),
            # Desarrollo y calidad
            ("pytest", "Tests automatizados", "🧪 Desarrollo", "", "https://docs.pytest.org/"),
            ("black", "Formateador de código (estilo uniforme)", "🧪 Desarrollo", "", "https://black.readthedocs.io/"),
            ("autopep8", "Formatear según PEP 8", "🧪 Desarrollo", "", "https://github.com/hhatto/autopep8"),
            ("isort", "Ordenar imports automáticamente", "🧪 Desarrollo", "", "https://pycqa.github.io/isort/"),
            ("ruff", "Linter y formateador muy rápido", "🧪 Desarrollo", "", "https://docs.astral.sh/ruff/"),
            ("mypy", "Comprobación de tipos estáticos", "🧪 Desarrollo", "", "https://mypy.readthedocs.io/"),
            # Incluidos en Python (referencia, no se instalan con pip)
            ("tkinter", "Interfaz gráfica básica (stdlib)", "✅ Incluido en Python", "", "", "tkinter", True),
            ("sqlite3", "Base de datos SQLite (stdlib)", "✅ Incluido en Python", "", "", "sqlite3", True),
        ]

        packages: Dict[str, PackageInfo] = {}
        for entry in catalog:
            pip_name = entry[0]
            desc = entry[1]
            category = entry[2]
            author = entry[3] if len(entry) > 3 else ""
            home = entry[4] if len(entry) > 4 else ""
            install_name = entry[5] if len(entry) > 5 and entry[5] is not None else pip_name
            builtin = entry[6] if len(entry) > 6 else False
            packages[pip_name] = PackageInfo(
                name=pip_name,
                description=desc,
                author=author,
                home_page=home,
                category=category,
                pip_name=install_name,
                builtin=builtin,
                installed=builtin,
                version="Built-in" if builtin else "",
            )
        return packages
    
    def _update_installed_packages(self):
        """Actualiza la lista de paquetes instalados"""
        self.installed_packages = {}
        
        try:
            if METADATA_AVAILABLE and distributions:
                # Usar importlib.metadata para obtener paquetes instalados
                for dist in distributions():
                    package_name = dist.metadata['Name'].lower()
                    self.installed_packages[package_name] = PackageInfo(
                        name=package_name,
                        version=dist.version,
                        installed=True
                    )
                    
                    # Actualizar paquetes populares si están instalados
                    if package_name in self.popular_packages:
                        self.popular_packages[package_name].installed = True
                        self.popular_packages[package_name].version = dist.version
            else:
                # Método alternativo usando pip list
                try:
                    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                          capture_output=True, text=True, check=True)
                    installed_packages = json.loads(result.stdout)
                    
                    for package in installed_packages:
                        package_name = package['name'].lower()
                        self.installed_packages[package_name] = PackageInfo(
                            name=package_name,
                            version=package['version'],
                            installed=True
                        )
                        
                        # Actualizar paquetes populares si están instalados
                        if package_name in self.popular_packages:
                            self.popular_packages[package_name].installed = True
                            self.popular_packages[package_name].version = package['version']
                except subprocess.CalledProcessError:
                    print("No se pudo obtener la lista de paquetes instalados")
                    
        except Exception as e:
            print(f"Error al obtener paquetes instalados: {e}")
    
    def search_package(self, package_name: str) -> Optional[PackageInfo]:
        """Busca información de un paquete en PyPI"""
        try:
            if not REQUESTS_AVAILABLE or not requests:
                # Crear una respuesta básica sin usar requests
                is_installed = package_name.lower() in self.installed_packages
                current_version = ""
                if is_installed:
                    current_version = self.installed_packages[package_name.lower()].version
                
                return PackageInfo(
                    name=package_name,
                    version=current_version,
                    description=f"Paquete {package_name}",
                    installed=is_installed
                )
            
            # Buscar en PyPI usando requests
            response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=5)
            if response.status_code == 200:
                data = response.json()
                info = data.get('info', {})
                
                # Verificar si está instalado
                is_installed = package_name.lower() in self.installed_packages
                current_version = ""
                if is_installed:
                    current_version = self.installed_packages[package_name.lower()].version
                
                return PackageInfo(
                    name=info.get('name', package_name),
                    version=current_version,
                    description=info.get('summary', 'No hay descripción disponible'),
                    author=info.get('author', 'Desconocido'),
                    home_page=info.get('home_page', ''),
                    installed=is_installed,
                    latest_version=info.get('version', '')
                )
        except Exception as e:
            print(f"Error al buscar paquete {package_name}: {e}")
        
        return None
    
    def install_package(self, package_name: str, callback=None) -> Dict:
        """Instala un paquete usando pip"""
        try:
            if callback:
                callback(f"Instalando {package_name}...")
            
            # Comando pip install
            cmd = [sys.executable, '-m', 'pip', 'install', package_name]
            
            # Ejecutar comando
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutos timeout
            )
            
            if result.returncode == 0:
                # Actualizar lista de paquetes instalados
                self._update_installed_packages()
                
                if callback:
                    callback(f"✅ {package_name} instalado correctamente")
                
                return {
                    'success': True,
                    'message': f'Paquete {package_name} instalado correctamente',
                    'output': result.stdout
                }
            else:
                error_msg = result.stderr or result.stdout or 'Error desconocido'
                if callback:
                    callback(f"❌ Error instalando {package_name}: {error_msg}")
                
                return {
                    'success': False,
                    'message': f'Error al instalar {package_name}',
                    'error': error_msg
                }
                
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'message': 'La instalación tardó demasiado tiempo',
                'error': 'Timeout'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error inesperado: {str(e)}',
                'error': str(e)
            }
    
    def uninstall_package(self, package_name: str, callback=None) -> Dict:
        """Desinstala un paquete usando pip"""
        try:
            if callback:
                callback(f"Desinstalando {package_name}...")
            
            # Comando pip uninstall
            cmd = [sys.executable, '-m', 'pip', 'uninstall', package_name, '-y']
            
            # Ejecutar comando
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                # Actualizar lista de paquetes instalados
                self._update_installed_packages()
                
                if callback:
                    callback(f"✅ {package_name} desinstalado correctamente")
                
                return {
                    'success': True,
                    'message': f'Paquete {package_name} desinstalado correctamente',
                    'output': result.stdout
                }
            else:
                error_msg = result.stderr or result.stdout or 'Error desconocido'
                if callback:
                    callback(f"❌ Error desinstalando {package_name}: {error_msg}")
                
                return {
                    'success': False,
                    'message': f'Error al desinstalar {package_name}',
                    'error': error_msg
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'Error inesperado: {str(e)}',
                'error': str(e)
            }
    
    def upgrade_package(self, package_name: str, callback=None) -> Dict:
        """Actualiza un paquete a la última versión"""
        try:
            if callback:
                callback(f"Actualizando {package_name}...")
            
            # Comando pip install --upgrade
            cmd = [sys.executable, '-m', 'pip', 'install', '--upgrade', package_name]
            
            # Ejecutar comando
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                # Actualizar lista de paquetes instalados
                self._update_installed_packages()
                
                if callback:
                    callback(f"✅ {package_name} actualizado correctamente")
                
                return {
                    'success': True,
                    'message': f'Paquete {package_name} actualizado correctamente',
                    'output': result.stdout
                }
            else:
                error_msg = result.stderr or result.stdout or 'Error desconocido'
                if callback:
                    callback(f"❌ Error actualizando {package_name}: {error_msg}")
                
                return {
                    'success': False,
                    'message': f'Error al actualizar {package_name}',
                    'error': error_msg
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'Error inesperado: {str(e)}',
                'error': str(e)
            }
    
    def get_popular_packages_list(self) -> List[Dict]:
        """Retorna lista de paquetes populares con su estado"""
        packages = []
        for name, package in self.popular_packages.items():
            packages.append({
                'name': package.name,
                'description': package.description,
                'version': package.version,
                'installed': package.installed,
                'author': package.author,
                'home_page': package.home_page,
                'category': package.category,
                'pip_name': package.pip_name,
                'builtin': package.builtin,
            })
        
        return sorted(packages, key=lambda x: (x['category'], not x['installed'], x['name']))
    
    def get_categories(self) -> List[str]:
        """Categorías únicas del catálogo, ordenadas."""
        cats = sorted({p.category for p in self.popular_packages.values()})
        return cats
    
    def get_installed_packages_list(self) -> List[Dict]:
        """Retorna lista de todos los paquetes instalados"""
        packages = []
        for name, package in self.installed_packages.items():
            packages.append({
                'name': package.name,
                'version': package.version,
                'description': package.description,
                'installed': True
            })
        
        return sorted(packages, key=lambda x: x['name'])
    
    def _get_package_category(self, package_name: str) -> str:
        """Retorna la categoría de un paquete del catálogo."""
        pkg = self.popular_packages.get(package_name)
        if pkg:
            return pkg.category
        return "📦 General"
    
    def get_package_usage_examples(self, package_name: str) -> List[str]:
        """Retorna ejemplos de uso para paquetes populares"""
        examples = {
            'requests': [
                '# Petición GET\nimport requests\nr = requests.get("https://api.github.com")\nprint(r.status_code)',
            ],
            'httpx': [
                '# HTTP async\nimport httpx\nimport asyncio\n\nasync def main():\n    async with httpx.AsyncClient() as client:\n        r = await client.get("https://httpbin.org/get")\n        print(r.json())\n\nasyncio.run(main())',
            ],
            'matplotlib': [
                '# Gráfico de líneas\nimport matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [1, 4, 2])\nplt.title("Mi gráfico")\nplt.show()',
            ],
            'pandas': [
                '# DataFrame desde diccionario\nimport pandas as pd\ndf = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [25, 30]})\nprint(df)',
            ],
            'flask': [
                'from flask import Flask\napp = Flask(__name__)\n\n@app.route("/")\ndef inicio():\n    return "Hola desde Flask"\n\nif __name__ == "__main__":\n    app.run(debug=True)',
            ],
            'fastapi': [
                'from fastapi import FastAPI\napp = FastAPI()\n\n@app.get("/")\ndef leer_raiz():\n    return {"mensaje": "Hola API"}\n\n# Ejecutar: uvicorn main:app --reload',
            ],
            'rich': [
                'from rich.console import Console\nfrom rich.table import Table\n\nconsole = Console()\ntable = Table(title="Usuarios")\ntable.add_column("Nombre")\ntable.add_row("Ana")\nconsole.print(table)',
            ],
            'pytest': [
                '# test_suma.py\ndef suma(a, b):\n    return a + b\n\ndef test_suma():\n    assert suma(2, 3) == 5\n\n# Ejecutar: pytest test_suma.py',
            ],
            'python-dotenv': [
                '# .env → VARIABLE=valor\nfrom dotenv import load_dotenv\nimport os\n\nload_dotenv()\nprint(os.getenv("VARIABLE"))',
            ],
            'pillow': [
                'from PIL import Image\nimg = Image.open("foto.jpg")\nimg.thumbnail((200, 200))\nimg.save("miniatura.jpg")',
            ],
        }
        return examples.get(package_name, ['# Consulta la documentación oficial del paquete para ejemplos.'])

class PackageManagerUI:
    """Interfaz para el gestor de paquetes"""
    
    def __init__(self):
        self.package_manager = PackageManager()
        self.current_operation = None
    
    def get_popular_packages(self) -> List[Dict]:
        """Obtiene paquetes populares para mostrar en la UI"""
        return self.package_manager.get_popular_packages_list()
    
    def get_installed_packages(self) -> List[Dict]:
        """Obtiene paquetes instalados para mostrar en la UI"""
        return self.package_manager.get_installed_packages_list()
    
    def get_categories(self) -> List[str]:
        """Categorías del catálogo para filtros en la UI."""
        return self.package_manager.get_categories()
    
    def get_package_by_key(self, key: str) -> Optional[Dict]:
        """Devuelve un paquete del catálogo por clave interna."""
        pkg = self.package_manager.popular_packages.get(key)
        if not pkg:
            return None
        return {
            'key': key,
            'name': pkg.name,
            'pip_name': pkg.pip_name,
            'description': pkg.description,
            'installed': pkg.installed,
            'builtin': pkg.builtin,
            'category': pkg.category,
            'examples': self.package_manager.get_package_usage_examples(pkg.name),
        }

    def install_package_async(self, package_name: str, progress_callback=None) -> Dict:
        """Instala un paquete de forma asíncrona"""
        def install_thread():
            return self.package_manager.install_package(package_name, progress_callback)
        
        # En una implementación real, esto se ejecutaría en un hilo separado
        return self.package_manager.install_package(package_name, progress_callback)
    
    def search_package_info(self, package_name: str) -> Optional[Dict]:
        """Busca información de un paquete"""
        package_info = self.package_manager.search_package(package_name)
        if package_info:
            return {
                'name': package_info.name,
                'version': package_info.version,
                'description': package_info.description,
                'author': package_info.author,
                'home_page': package_info.home_page,
                'installed': package_info.installed,
                'latest_version': package_info.latest_version,
                'examples': self.package_manager.get_package_usage_examples(package_info.name)
            }
        return None

# Función helper para la UI
def get_package_manager() -> PackageManagerUI:
    """Retorna una instancia del gestor de paquetes para la UI"""
    return PackageManagerUI()
