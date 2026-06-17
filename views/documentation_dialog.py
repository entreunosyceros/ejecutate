#!/usr/bin/env python3
"""
Diálogo de documentación que muestra información completa sobre cómo usar la aplicación
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QScrollArea, 
                               QLabel, QPushButton, QTextEdit, QTabWidget, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QIcon

class DocumentationDialog(QDialog):
    """Diálogo que muestra la documentación completa de la aplicación"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📚 Documentación - Editor de Código Python")
        self.setModal(True)
        self.resize(800, 700)
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz del diálogo"""
        layout = QVBoxLayout(self)
        
        # Título principal
        title_label = QLabel("📚 Guía Completa del Editor de Código Python")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2C3E50;
                padding: 15px;
                background-color: #ECF0F1;
                border-radius: 8px;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(title_label)
        
        # Widget con pestañas para organizar la documentación
        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #BDC3C7;
                border-radius: 5px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #ECF0F1;
                color: #2C3E50;
                padding: 10px 15px;
                margin-right: 2px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                border: 1px solid #BDC3C7;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #3498DB;
                color: white;
                border-bottom: none;
            }
            QTabBar::tab:hover {
                background-color: #D5DBDB;
            }
        """)
        
        # Pestaña 1: Introducción
        intro_tab = self.create_intro_tab()
        tab_widget.addTab(intro_tab, "🏠 Introducción")
        
        # Pestaña 2: Editor de Código
        editor_tab = self.create_editor_tab()
        tab_widget.addTab(editor_tab, "📝 Editor")
        
        # Pestaña 3: Terminal
        terminal_tab = self.create_terminal_tab()
        tab_widget.addTab(terminal_tab, "💻 Terminal")
        
        # Pestaña 4: Funciones Educativas
        educational_tab = self.create_educational_tab()
        tab_widget.addTab(educational_tab, "🎓 Aprendizaje")
        
        # Pestaña 5: Características Avanzadas
        features_tab = self.create_features_tab()
        tab_widget.addTab(features_tab, "⚡ Funciones")
        
        # Pestaña 6: Atajos de Teclado
        shortcuts_tab = self.create_shortcuts_tab()
        tab_widget.addTab(shortcuts_tab, "⌨️ Atajos")
        
        layout.addWidget(tab_widget)
        
        # Botón para cerrar
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        close_button = QPushButton("✅ Cerrar")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                padding: 10px 30px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
    
    def create_scrollable_content(self, content):
        """Crea un área de scroll con contenido HTML"""
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(content)
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #2C3E50;
                border: none;
                padding: 15px;
                font-size: 13px;
                line-height: 1.4;
            }
        """)
        
        scroll_area.setWidget(text_edit)
        return scroll_area
    
    def create_intro_tab(self):
        """Crea la pestaña de introducción"""
        content = """
        <h2 style="color: #2C3E50;">🎉 ¡Bienvenido al Editor de Código Python!</h2>
        
        <p>Este editor está diseñado para hacer que programar en Python sea <strong>fácil</strong>, <strong>cómodo</strong> y <strong>productivo</strong>.</p>
        
        <h3 style="color: #E74C3C;">🌟 Características Principales:</h3>
        <ul>
            <li><strong>📝 Editor con Pestañas:</strong> Trabajo con múltiples archivos simultáneamente</li>
            <li><strong>🎨 Resaltado de Sintaxis:</strong> Código Python con colores para mejor legibilidad</li>
            <li><strong>💻 Terminal Integrado:</strong> Ejecuta código directamente sin salir del editor</li>
            <li><strong>🔍 Búsqueda Avanzada:</strong> Busca y reemplaza texto en archivos individuales o múltiples</li>
            <li><strong>🎯 Formateo Automático:</strong> Código limpio según estándares PEP 8</li>
            <li><strong>📁 Explorador de Archivos:</strong> Navega por tu proyecto fácilmente</li>
            <li><strong>💾 Gestión de Sesiones:</strong> Guarda y restaura tu trabajo automáticamente</li>
        </ul>
        
        <h3 style="color: #27AE60;">🚀 ¿Cómo Empezar?</h3>
        <ol>
            <li><strong>Escribir Código:</strong> Usa el área de texto principal para escribir tu código Python</li>
            <li><strong>Ejecutar:</strong> Presiona <code>Ctrl+Enter</code> o el botón "🚀 Ejecutar Código"</li>
            <li><strong>Ver Resultados:</strong> La salida aparece directamente en el terminal integrado</li>
            <li><strong>Interactuar:</strong> El terminal soporta input() y comandos interactivos</li>
        </ol>
        
        <div style="background-color: #D5DBDB; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo:</strong> Explora las otras pestañas de esta documentación para aprender sobre todas las funciones disponibles.
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_editor_tab(self):
        """Crea la pestaña del editor"""
        content = """
        <h2 style="color: #2C3E50;">📝 Editor de Código</h2>
        
        <h3 style="color: #E74C3C;">🔖 Sistema de Pestañas</h3>
        <ul>
            <li><strong>Nuevo:</strong> <code>Ctrl+N</code> o Menú → Archivo → Nuevo (también <code>Ctrl+T</code>)</li>
            <li><strong>Abrir archivo:</strong> <code>Ctrl+O</code>, explorador (doble clic) o Menú → Archivo → Abrir archivo…</li>
            <li><strong>Abrir carpeta:</strong> <code>Ctrl+Shift+O</code> o Menú → Archivo → Abrir carpeta…</li>
            <li><strong>Pestaña inicial:</strong> si «Nuevo 1» está vacía, al abrir un archivo se reutiliza esa pestaña</li>
            <li><strong>Cerrar Pestaña:</strong> <code>Ctrl+W</code> o click en la "❌" de la pestaña (si hay cambios sin guardar, pregunta Guardar / No / Cancelar)</li>
            <li><strong>Indicador de cambios:</strong> un prefijo <code>•</code> en el título de la pestaña significa que no está guardada</li>
            <li><strong>Cambiar entre Pestañas:</strong> Click en las pestañas o <code>Ctrl+Tab</code></li>
        </ul>
        
        <h3 style="color: #E74C3C;">📁 Carpeta de trabajo</h3>
        <ul>
            <li>La ruta de la carpeta del explorador aparece en la barra superior, junto a «Ejecútalo!»</li>
            <li>Al abrir archivos desde el explorador no se muestran ventanas de confirmación</li>
        </ul>
        
        <h3 style="color: #E74C3C;">📄 Markdown y texto</h3>
        <ul>
            <li><strong>Archivos .md:</strong> vista previa opcional con <code>Ctrl+Shift+V</code> o Vista → Vista previa Markdown</li>
            <li><strong>.txt y .md:</strong> no permiten ejecutar código con <code>Ctrl+Enter</code></li>
            <li><strong>Explorador:</strong> iconos distintos por tipo de archivo</li>
        </ul>
        
        <h3 style="color: #E74C3C;">💾 Guardar y Abrir Archivos</h3>
        <ul>
            <li><strong>Nuevo:</strong> <code>Ctrl+N</code> — pestaña vacía</li>
            <li><strong>Abrir Archivo:</strong> <code>Ctrl+O</code> o Menú → Archivo → Abrir archivo…</li>
            <li><strong>Abrir Carpeta:</strong> <code>Ctrl+Shift+O</code> o Menú → Archivo → Abrir carpeta…</li>
            <li><strong>Guardar:</strong> <code>Ctrl+S</code> o Menú → Archivo → Guardar</li>
            <li><strong>Guardar Como:</strong> <code>Ctrl+Shift+S</code> o Menú → Archivo → Guardar Como</li>
        </ul>
        
        <h3 style="color: #E74C3C;">🎨 Resaltado de Sintaxis</h3>
        <p>El editor automáticamente resalta:</p>
        <ul>
            <li><strong style="color: blue;">Palabras clave de Python:</strong> def, class, if, for, etc.</li>
            <li><strong style="color: green;">Comentarios:</strong> Líneas que comienzan con #</li>
            <li><strong style="color: red;">Cadenas de texto:</strong> Texto entre comillas</li>
            <li><strong style="color: purple;">Números:</strong> Valores numéricos</li>
        </ul>
        
        <h3 style="color: #E74C3C;">🔧 Formateo de Código</h3>
        <ul>
            <li><strong>Formatear Manualmente:</strong> <code>Ctrl+Alt+F</code> o Menú → Editar → Formatear Código</li>
            <li><strong>Configurar Formateo:</strong> Menú → Editar → Preferencias → Pestaña Formatter</li>
            <li><strong>Motores Disponibles:</strong> Manual, autopep8, black</li>
        </ul>
        
        <h3 style="color: #E74C3C;">🔍 Búsqueda y Reemplazo</h3>
        <ul>
            <li><strong>Buscar:</strong> <code>Ctrl+F</code> - Busca texto en el archivo actual</li>
            <li><strong>Buscar y Reemplazar:</strong> <code>Ctrl+H</code> - Reemplaza texto en el archivo actual</li>
            <li><strong>Buscar en Múltiples Archivos:</strong> <code>Ctrl+Shift+F</code> - Busca en todo el proyecto</li>
        </ul>
        
        <div style="background-color: #E8F6F3; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo:</strong> El editor guarda automáticamente tu trabajo y restaura las pestañas cuando reinicias la aplicación.
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_terminal_tab(self):
        """Crea la pestaña del terminal"""
        content = """
        <h2 style="color: #2C3E50;">💻 Terminal Integrado</h2>
        
        <h3 style="color: #8E44AD;">🔄 Tipos de Shell</h3>
        <p>El terminal soporta diferentes tipos de intérpretes:</p>
        <ul>
            <li><strong>🐍 Python3 Interactivo:</strong> Para ejecutar código Python línea por línea</li>
            <li><strong>🛠️ Bash:</strong> Para comandos del sistema (ls, cd, mkdir, etc.)</li>
            <li><strong>📜 Python3:</strong> Para ejecutar scripts Python completos</li>
        </ul>
        
        <h3 style="color: #8E44AD;">🚀 Ejecutar Código</h3>
        <p>Toda la ejecución se realiza a través del terminal integrado para máxima interactividad:</p>
        <ul>
            <li><strong>Desde el Editor:</strong> <code>Ctrl+Enter</code> o botón "🚀 Ejecutar Código"</li>
            <li><strong>Directamente en Terminal:</strong> Escribe código en el campo de entrada y presiona <code>Enter</code></li>
        </ul>
        
        <h3 style="color: #8E44AD;">🔤 Comandos de Terminal</h3>
        <h4>En modo Python:</h4>
        <div style="background-color: #f8f9fa; padding: 10px; border-left: 4px solid #28a745; margin: 10px 0;">
            <code>print("¡Hola mundo!")</code><br>
            <code>x = 5 + 3</code><br>
            <code>for i in range(5): print(i)</code><br>
            <code>import os; print(os.getcwd())</code>
        </div>
        
        <h4>En modo Bash:</h4>
        <div style="background-color: #f8f9fa; padding: 10px; border-left: 4px solid #007bff; margin: 10px 0;">
            <code>ls -la</code><br>
            <code>pwd</code><br>
            <code>mkdir mi_proyecto</code><br>
            <code>echo "Hola desde bash"</code><br>
            <code>nano archivo.txt</code> (Editor de texto en terminal)<br>
            <code>grep -r "texto" .</code> (Buscar en archivos)
        </div>
        
        <h3 style="color: #8E44AD;">🖥️ Aplicaciones Gráficas</h3>
        <p>El terminal soporta tanto comandos de consola como aplicaciones gráficas:</p>
        <ul>
            <li><strong>✅ Aplicaciones de terminal:</strong> nano, vim, htop, curl, wget, git</li>
            <li><strong>✅ Aplicaciones gráficas:</strong> gedit, firefox, calculator, file managers</li>
            <li><strong>✅ Herramientas de desarrollo:</strong> code, atom, sublime (si están instaladas)</li>
        </ul>
        
        <div style="background-color: #E3F2FD; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo para Aplicaciones Gráficas:</strong> El terminal preserva las variables de entorno necesarias para ejecutar aplicaciones gráficas como gedit, calculadora, navegadores, etc.
        </div>
        
        <h3 style="color: #8E44AD;">💬 Input Interactivo</h3>
        <p>Cuando tu código Python usa <code>input()</code>:</p>
        <ol>
            <li>Aparece el prompt en el terminal</li>
            <li>Se abre un cuadro de diálogo para introducir datos</li>
            <li>Tu respuesta se envía automáticamente al programa</li>
            <li>El código continúa ejecutándose normalmente</li>
        </ol>
        
        <h3 style="color: #8E44AD;">⚙️ Controles del Terminal</h3>
        <ul>
            <li><strong>🗑️ Limpiar:</strong> Borra toda la salida del terminal</li>
            <li><strong>🔄 Reiniciar:</strong> Reinicia completamente el intérprete</li>
            <li><strong>Cambiar Shell:</strong> Usa el dropdown para cambiar entre Python y Bash</li>
            <li><strong>🖥️ Terminal del Sistema:</strong> <code>Ctrl+Alt+T</code> o Menú → Vista → Abrir Terminal del Sistema</li>
        </ul>
        
        <div style="background-color: #E8F8F5; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo:</strong> Usa la opción "Terminal del Sistema" para acceder a la terminal nativa de tu sistema operativo (CMD/PowerShell en Windows, Terminal en macOS, o tu terminal favorito en Linux).
        </div>
        
        <div style="background-color: #FFF3CD; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>⚠️ Importante:</strong> 
            <ul>
                <li>En Python: usa comandos Python (print, input, import, etc.)</li>
                <li>En Bash: usa comandos del sistema (ls, cd, echo, etc.)</li>
                <li>No mezcles tipos de comandos en el mismo modo</li>
                <li>Para editar archivos: usa <code>nano</code> (terminal) o <code>gedit</code> (gráfico)</li>
            </ul>
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_educational_tab(self):
        """Crea la pestaña de funciones educativas"""
        content = """
        <h2 style="color: #2C3E50;">🎓 Funciones de Aprendizaje</h2>
        
        <p>El editor incluye <strong>5 funcionalidades educativas especiales</strong> diseñadas para ayudar a principiantes a aprender Python de manera efectiva.</p>
        
        <h3 style="color: #8E44AD;">🔍 Análisis de Código en Tiempo Real (F7)</h3>
        <p>Obtén feedback inmediato mientras escribes código:</p>
        <ul>
            <li><strong>Detección automática de errores</strong> de sintaxis</li>
            <li><strong>Sugerencias de mejora</strong> según buenas prácticas</li>
            <li><strong>Clasificación clara</strong>: errores ❌, advertencias ⚠️, sugerencias 💡</li>
            <li><strong>Explicaciones educativas</strong> específicas para principiantes</li>
        </ul>
        
        <div style="background-color: #E8F6F3; padding: 10px; border-left: 4px solid #27AE60; margin: 10px 0;">
            <strong>📋 Tipos de análisis incluidos:</strong><br>
            • Errores de sintaxis básicos<br>
            • Código Python 2 vs Python 3<br>
            • Nombres de variables según convenciones<br>
            • Líneas demasiado largas<br>
            • Sugerencias de f-strings<br>
            • Detección de bucles infinitos potenciales
        </div>
        
        <h3 style="color: #8E44AD;">💡 Autocompletado Inteligente</h3>
        <p>Sugerencias contextuales con explicaciones educativas:</p>
        <ul>
            <li><strong>17 funciones built-in</strong> con ejemplos (print, input, len, etc.)</li>
            <li><strong>15 palabras clave</strong> de Python con explicaciones (if, for, def, etc.)</li>
            <li><strong>10 snippets</strong> de código común predefinidos</li>
            <li><strong>Ejemplos prácticos</strong> para cada sugerencia</li>
        </ul>
        
        <h3 style="color: #8E44AD;">📚 Tutoriales Interactivos (F4)</h3>
        <p>Aprende Python paso a paso con tutoriales guiados:</p>
        
        <h4>📖 Tutoriales Disponibles:</h4>
        <ol>
            <li><strong>"Primeros pasos con Python"</strong> (Principiante - 4 pasos)
                <ul>
                    <li>Hola mundo y función print()</li>
                    <li>Variables y tipos de datos</li>
                    <li>Operaciones matemáticas básicas</li>
                    <li>Entrada de usuario con input()</li>
                </ul>
            </li>
            <li><strong>"Estructuras de control"</strong> (Principiante - 4 pasos)
                <ul>
                    <li>Decisiones con if/else</li>
                    <li>Múltiples condiciones con elif</li>
                    <li>Bucles con for</li>
                    <li>Bucles con while</li>
                </ul>
            </li>
            <li><strong>"Listas y funciones"</strong> (Intermedio - 4 pasos)
                <ul>
                    <li>Trabajando con listas</li>
                    <li>Modificando listas</li>
                    <li>Creando funciones</li>
                    <li>Funciones que retornan valores</li>
                </ul>
            </li>
        </ol>
        
        <h3 style="color: #8E44AD;">🐛 Debugger Visual (F5)</h3>
        <p>Ejecuta tu código paso a paso para entender cómo funciona:</p>
        <ul>
            <li><strong>▶️ Ejecutar paso a paso</strong>: Ve línea por línea</li>
            <li><strong>📊 Inspección de variables</strong>: Ve valores en tiempo real</li>
            <li><strong>🚀 Ejecutar hasta breakpoint</strong>: Control de paradas</li>
            <li><strong>📤 Captura de salida</strong>: Ve qué imprime tu programa</li>
        </ul>
        
        <h3 style="color: #8E44AD;">📦 Gestor de Paquetes Visual (F6)</h3>
        <p>Instala y gestiona paquetes Python de forma fácil:</p>
        <ul>
            <li><strong>15 paquetes populares</strong> curados para principiantes</li>
            <li><strong>Instalación con un clic</strong></li>
            <li><strong>Información detallada</strong> de cada paquete</li>
            <li><strong>Ejemplos de uso</strong> incluidos</li>
        </ul>
        
        <div style="background-color: #E3F2FD; padding: 10px; border-left: 4px solid #2196F3; margin: 10px 0;">
            <strong>🌟 Paquetes destacados incluidos:</strong><br>
            📊 matplotlib - Crear gráficos<br>
            🌐 requests - Peticiones web<br>
            📈 pandas - Análisis de datos<br>
            🔢 numpy - Matemáticas<br>
            🖼️ pillow - Manipular imágenes<br>
            🎮 pygame - Crear juegos
        </div>
        
        <h3 style="color: #8E44AD;">🚀 Cómo Empezar</h3>
        <ol>
            <li><strong>Análisis automático:</strong> Presiona <code>F7</code> para activar el análisis en tiempo real</li>
            <li><strong>Primer tutorial:</strong> Presiona <code>F4</code> y selecciona "Primeros pasos con Python"</li>
            <li><strong>Debuggear código:</strong> Escribe código y presiona <code>F5</code> para ejecutar paso a paso</li>
            <li><strong>Instalar paquetes:</strong> Presiona <code>F6</code> para explorar paquetes populares</li>
        </ol>
        
        <div style="background-color: #FFF3CD; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo para Principiantes:</strong> Empieza activando el análisis de código (F7) y luego sigue el primer tutorial (F4). ¡El editor te guiará en tu aprendizaje!
        </div>
        
        <h3 style="color: #8E44AD;">🎯 Beneficios Educativos</h3>
        <ul>
            <li><strong>Aprendizaje activo:</strong> Feedback inmediato mientras programas</li>
            <li><strong>Progresión estructurada:</strong> Tutoriales del nivel básico al intermedio</li>
            <li><strong>Comprensión profunda:</strong> Ve cómo se ejecuta tu código paso a paso</li>
            <li><strong>Herramientas reales:</strong> Aprende a usar paquetes populares</li>
            <li><strong>Buenas prácticas:</strong> Sugerencias basadas en estándares de Python</li>
        </ul>
        """
        return self.create_scrollable_content(content)
    
    def create_features_tab(self):
        """Crea la pestaña de características avanzadas"""
        content = """
        <h2 style="color: #2C3E50;">⚡ Funciones Avanzadas</h2>
        
        <h3 style="color: #F39C12;">📁 Explorador de Archivos</h3>
        <ul>
            <li><strong>Mostrar/Ocultar:</strong> <code>F3</code> o Menú → Vista → Explorador de Archivos</li>
            <li><strong>Navegar Carpetas:</strong> Click en carpetas para expandir/contraer</li>
            <li><strong>Abrir Archivo:</strong> Doble click en un archivo Python</li>
            <li><strong>Actualizar:</strong> Botón de actualización para ver cambios</li>
        </ul>
        
        <h3 style="color: #F39C12;">💾 Gestión de Sesiones</h3>
        <p>La aplicación guarda automáticamente:</p>
        <ul>
            <li>Archivos abiertos en pestañas</li>
            <li>Posición de las ventanas</li>
            <li>Configuraciones del editor</li>
            <li>Historial de archivos recientes</li>
        </ul>
        
        <h4>Controles Manuales:</h4>
        <ul>
            <li><strong>Guardar Sesión:</strong> Menú → Sesión → Guardar Sesión</li>
            <li><strong>Restaurar Sesión:</strong> Menú → Sesión → Restaurar Sesión</li>
            <li><strong>Archivos Recientes:</strong> Menú → Sesión → Archivos Recientes</li>
            <li><strong>Limpiar Sesión:</strong> Menú → Sesión → Limpiar Sesión</li>
        </ul>
        
        <h3 style="color: #F39C12;">🎨 Personalización</h3>
        <p>Accede a Menú → Editar → Preferencias para configurar:</p>
        
        <h4>Editor:</h4>
        <ul>
            <li>Fuente y tamaño de letra</li>
            <li>Colores de fondo y texto</li>
            <li>Color de selección</li>
            <li>Colores de numeración de líneas</li>
        </ul>
        
        <h4>Área de Salida:</h4>
        <ul>
            <li>Fuente y tamaño para resultados</li>
            <li>Colores de fondo y texto de salida</li>
        </ul>
        
        <h4>Formatter:</h4>
        <ul>
            <li>Habilitar/deshabilitar formateo automático</li>
            <li>Motor de formateo (autopep8, black)</li>
            <li>Longitud máxima de línea</li>
            <li>Tamaño de indentación</li>
            <li>Organizar imports automáticamente</li>
        </ul>
        
        <h3 style="color: #F39C12;">🔍 Búsqueda Avanzada</h3>
        
        <h4>Búsqueda Simple (<code>Ctrl+F</code>):</h4>
        <ul>
            <li>Busca texto en el archivo actual</li>
            <li>Navegación con botones Anterior/Siguiente</li>
            <li>Búsqueda sensible a mayúsculas (opcional)</li>
        </ul>
        
        <h4>Buscar y Reemplazar (<code>Ctrl+H</code>):</h4>
        <ul>
            <li>Reemplaza texto en el archivo actual</li>
            <li>Reemplazo individual o masivo</li>
            <li>Vista previa antes de reemplazar</li>
        </ul>
        
        <h4>Búsqueda en Múltiples Archivos (<code>Ctrl+Shift+F</code>):</h4>
        <ul>
            <li>Busca en toda una carpeta o proyecto</li>
            <li>Filtros por tipo de archivo</li>
            <li>Resultados organizados por archivo</li>
            <li>Click en resultados para abrir archivo</li>
        </ul>
        
        <h3 style="color: #F39C12;">🔔 Bandeja del Sistema</h3>
        <ul>
            <li>Minimiza la aplicación a la bandeja del sistema</li>
            <li>Doble click en el icono para restaurar</li>
            <li>Menú contextual con opciones rápidas</li>
            <li>Notificaciones de sistema</li>
        </ul>
        
        <div style="background-color: #E8F6F3; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo Avanzado:</strong> Combina el explorador de archivos con la búsqueda en múltiples archivos para navegar eficientemente en proyectos grandes.
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_shortcuts_tab(self):
        """Crea la pestaña de atajos de teclado"""
        content = """
        <h2 style="color: #2C3E50;">⌨️ Atajos de Teclado</h2>
        
        <h3 style="color: #E67E22;">🚀 Ejecución de Código</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Enter</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Ejecutar código en terminal integrado</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + L</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Limpiar salida</td>
            </tr>
        </table>
        
        <h3 style="color: #E67E22;">📁 Gestión de Archivos</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + O</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir archivo</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + S</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Guardar archivo</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + S</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Guardar como</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + T</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Nueva pestaña</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + W</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Cerrar pestaña</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Q</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Salir de la aplicación</td>
            </tr>
        </table>
        
        <h3 style="color: #E67E22;">🔍 Búsqueda</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + F</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Buscar en archivo actual</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + H</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Buscar y reemplazar</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + F</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Buscar en múltiples archivos</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F3</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Buscar siguiente</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Shift + F3</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Buscar anterior</td>
            </tr>
        </table>
        
        <h3 style="color: #E67E22;">🔧 Edición y Formato</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Alt + F</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Formatear código</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + ,</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir preferencias</td>
            </tr>
        </table>
        
        <h3 style="color: #E67E22;">👁️ Vista y Navegación</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F3</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Mostrar/ocultar explorador de archivos</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + `</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Alternar entre salida y terminal</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Alt + T</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir terminal del sistema operativo</td>
            </tr>
        </table>
        
        <h3 style="color: #E67E22;">❓ Ayuda y Aprendizaje</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Atajo</th>
                <th style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">Función</th>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F1</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Mostrar información About</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F2</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Mostrar esta documentación</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F4</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">🎓 Tutoriales Interactivos</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F5</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">🐛 Debugger Visual</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F6</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">📦 Gestor de Paquetes</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>F7</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">🔍 Análisis de Código (activar/desactivar)</td>
            </tr>
        </table>
        
        <div style="background-color: #E8F8F5; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Tip Pro:</strong> La mayoría de estos atajos funcionan en cualquier momento, sin importar dónde tengas el cursor. ¡Memoriza los que más uses para ser súper productivo!
        </div>
        """
        return self.create_scrollable_content(content)
