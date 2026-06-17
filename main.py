#!/usr/bin/env python3
"""
Ejecútate! — Editor de código Python con arquitectura MVC
Versión PySide6 con resaltado de sintaxis
"""

import sys
import os
import argparse

# Añadir el directorio actual al path para importar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def check_dependencies():
    """Verifica qué dependencias están disponibles"""
    pyside_available = False
    pygments_available = False
    
    try:
        import PySide6
        pyside_available = True
        print("✅ PySide6 detectado")
    except ImportError:
        print("❌ PySide6 no está instalado")
    
    try:
        import pygments
        pygments_available = True
        print("✅ Pygments detectado")
    except ImportError:
        print("❌ Pygments no está instalado")
    
    return pyside_available, pygments_available


def install_dependencies():
    """Instala las dependencias requeridas"""
    print("\n🔧 Instalando dependencias...")
    import subprocess
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PySide6>=6.5.0", "Pygments>=2.15.0"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False


def main():
    """Función principal que inicia la aplicación"""
    parser = argparse.ArgumentParser(description="Ejecútate! — Editor de código Python con PySide6")
    parser.add_argument("--install-deps", action="store_true",
                       help="Instalar dependencias automáticamente")
    parser.add_argument("--check-deps", action="store_true",
                       help="Verificar dependencias disponibles")
    
    args = parser.parse_args()
    
    if args.check_deps:
        print("🔍 Verificando dependencias...")
        check_dependencies()
        return
    
    # Verificar dependencias
    pyside_available, pygments_available = check_dependencies()
    
    # Instalar dependencias si se solicita
    if args.install_deps:
        if not (pyside_available and pygments_available):
            if install_dependencies():
                pyside_available, pygments_available = check_dependencies()
    
    # Verificar que las dependencias están disponibles
    if not (pyside_available and pygments_available):
        print("\n❌ Error: PySide6 y Pygments son requeridos para ejecutar esta aplicación.")
        print("\n💡 Soluciones:")
        print("1. Instalar dependencias: python main.py --install-deps")
        print("2. Instalar manualmente: pip install PySide6 Pygments")
        print("3. Usar entorno virtual: source .venv/bin/activate && pip install PySide6 Pygments")
        print("4. Ejecutar con run_app.py: python run_app.py")
        sys.exit(1)
    
    try:
        print("🚀 Iniciando Ejecútate! (PySide6, resaltado de sintaxis)...")
        from controllers.editor_controller import CodeEditorController
        app = CodeEditorController()
        app.run()
        
    except KeyboardInterrupt:
        print("\n¡Aplicación cerrada por el usuario!")
    except Exception as e:
        print(f"Error fatal: {e}")
        print("\n💡 Sugerencias:")
        print("- Ejecuta: python main.py --install-deps")
        print("- Verifica dependencias: python main.py --check-deps")
        print("- Usa el launcher: python run_app.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
