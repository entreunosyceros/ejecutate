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
        self.setWindowTitle("📚 Documentación - Ejecútate!")
        self.setModal(True)
        self.resize(800, 700)
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz del diálogo"""
        layout = QVBoxLayout(self)
        
        # Título principal
        title_label = QLabel("📚 Guía Completa de Ejecútate!")
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
        
        # Pestaña 3: Interfaz (Activity Bar, paneles)
        interface_tab = self.create_interface_tab()
        tab_widget.addTab(interface_tab, "🖥️ Interfaz")
        
        # Pestaña 4: Terminal
        terminal_tab = self.create_terminal_tab()
        tab_widget.addTab(terminal_tab, "💻 Terminal")
        
        # Pestaña 5: Funciones Educativas
        educational_tab = self.create_educational_tab()
        tab_widget.addTab(educational_tab, "🎓 Aprendizaje")
        
        # Pestaña 6: Características Avanzadas
        features_tab = self.create_features_tab()
        tab_widget.addTab(features_tab, "⚡ Funciones")
        
        # Pestaña 7: Atajos de Teclado
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
        <h2 style="color: #2C3E50;">🎉 ¡Bienvenido a Ejecútate!</h2>
        
        <p>Este editor está diseñado para hacer que programar en Python sea <strong>fácil</strong>, <strong>cómodo</strong> y <strong>productivo</strong>.</p>
        
        <h3 style="color: #E74C3C;">🌟 Características Principales:</h3>
        <ul>
            <li><strong>📝 Editor con Pestañas:</strong> Varios archivos a la vez, indicador <code>•</code> si hay cambios sin guardar</li>
            <li><strong>🖥️ Interfaz tipo Cursor/VS Code:</strong> Activity Bar, sidebar (Explorer, Search, Problems, Outline, Aprendizaje) y panel inferior</li>
            <li><strong>🎨 Resaltado de Sintaxis:</strong> Palabras clave, cadenas, comentarios y números con colores del tema</li>
            <li><strong>⚠️ Problems:</strong> Errores y avisos del archivo Python (salto a línea/columna)</li>
            <li><strong>📋 Outline:</strong> Clases y funciones del archivo actual con salto rápido</li>
            <li><strong>💻 Terminal Integrado:</strong> Ejecuta el programa completo; programas interactivos usan la caja inferior</li>
            <li><strong>☕ Modo Café / Pomodoro:</strong> Pausas con overlay y temporizador configurable</li>
            <li><strong>🔍 Búsqueda Avanzada:</strong> En archivo, reemplazo y búsqueda en carpeta</li>
            <li><strong>🎯 Formateo Automático:</strong> PEP 8 con autopep8 o black</li>
            <li><strong>📁 Explorador y carpeta de trabajo:</strong> Ruta visible en la barra superior</li>
            <li><strong>🎓 Herramientas de aprendizaje:</strong> Tutoriales, debugger, paquetes y análisis (F4–F7)</li>
            <li><strong>💾 Sesiones:</strong> Restaura pestañas y preferencias al reiniciar</li>
        </ul>
        
        <h3 style="color: #27AE60;">🚀 ¿Cómo Empezar?</h3>
        <ol>
            <li><strong>Abrir carpeta:</strong> <code>Ctrl+Shift+O</code> para fijar la carpeta de trabajo del explorador</li>
            <li><strong>Escribir código:</strong> En el editor central (archivos <code>.py</code>)</li>
            <li><strong>Ejecutar:</strong> <code>Ctrl+Enter</code> o «🚀 Ejecutar Código» — lanza el programa entero en el terminal</li>
            <li><strong>Revisar errores:</strong> Pestaña <strong>Problems</strong> (sidebar o panel inferior) tras ~1 s sin escribir</li>
            <li><strong>Interactuar:</strong> Si el programa pide datos, escríbelos en la caja inferior del terminal</li>
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
            <li>La ruta de la carpeta del explorador aparece en la barra superior, junto a «Ejecútate!»</li>
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
        
        <h3 style="color: #E74C3C;">⚠️ Problems (errores y avisos)</h3>
        <p>Disponible en el <strong>sidebar</strong> (icono ! en la Activity Bar) y en el <strong>panel inferior</strong> (pestaña Problems).</p>
        <ul>
            <li><strong>ERROR:</strong> Sintaxis inválida (p. ej. paréntesis sin cerrar, falta <code>:</code>)</li>
            <li><strong>WARNING / INFO:</strong> Tras ~2,5 s sin escribir: imports no usados, variables sin usar, líneas largas, etc.</li>
            <li><strong>Badge:</strong> El icono Problems muestra el número de problemas del archivo actual</li>
            <li><strong>Salto:</strong> Doble clic en un ítem → cursor en esa línea/columna</li>
            <li><strong>Solo Python:</strong> No analiza <code>.md</code> ni <code>.txt</code></li>
            <li><strong>No incluye:</strong> Errores al ejecutar (esos aparecen en el Terminal)</li>
        </ul>
        
        <h3 style="color: #E74C3C;">📋 Outline (estructura del archivo)</h3>
        <ul>
            <li>Sidebar → pestaña <strong>Outline</strong> o icono en la Activity Bar</li>
            <li>Lista <strong>clases</strong> y <strong>funciones</strong> del <code>.py</code> activo</li>
            <li>Doble clic en un símbolo → salta a esa línea</li>
        </ul>
        
        <h3 style="color: #E74C3C;">💡 Autocompletado contextual</h3>
        <ul>
            <li>Sugerencias de palabras clave, builtins y snippets mientras escribes</li>
            <li><code>Tab</code> o <code>Enter</code> para aceptar; <code>Escape</code> para cerrar</li>
            <li>En líneas <code>import …</code> no sugiere builtins confusos (p. ej. <code>os</code> ≠ <code>OSError</code>)</li>
            <li>Se cierra al aceptar una sugerencia o al hacer clic fuera del editor</li>
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
    
    def create_interface_tab(self):
        """Crea la pestaña de interfaz (Activity Bar, paneles, Modo Café)"""
        content = """
        <h2 style="color: #2C3E50;">🖥️ Interfaz del Editor</h2>
        
        <p>La disposición recuerda a editores como <strong>Cursor</strong> o <strong>VS Code</strong>: barra lateral de iconos, sidebar con pestañas y panel inferior opcional.</p>
        
        <h3 style="color: #8E44AD;">📐 Layout general</h3>
        <ul>
            <li><strong>Barra superior:</strong> título «Ejecútate!», ruta de la carpeta de trabajo y botón <strong>☕</strong> (Modo Café)</li>
            <li><strong>Activity Bar</strong> (iconos verticales a la izquierda)</li>
            <li><strong>Sidebar</strong> (panel junto al editor, según el icono activo)</li>
            <li><strong>Editor central</strong> con pestañas de archivos</li>
            <li><strong>Panel inferior</strong> (Terminal, Problems, ayuda) — se puede ocultar</li>
            <li><strong>Barra de estado:</strong> línea/columna, tema y, con Pomodoro, cuenta atrás <code>☕ MM:SS</code></li>
        </ul>
        
        <h3 style="color: #8E44AD;">🧭 Activity Bar</h3>
        <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
            <tr style="background-color: #f8f9fa;">
                <th style="border: 1px solid #dee2e6; padding: 8px;">Icono</th>
                <th style="border: 1px solid #dee2e6; padding: 8px;">Vista en sidebar</th>
            </tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Explorer</td><td style="border: 1px solid #dee2e6; padding: 8px;">Árbol de archivos de la carpeta de trabajo</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Search</td><td style="border: 1px solid #dee2e6; padding: 8px;">Búsqueda en carpeta con resultados clicables</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Problems (!)</td><td style="border: 1px solid #dee2e6; padding: 8px;">Errores y avisos del archivo; badge con el conteo</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Outline</td><td style="border: 1px solid #dee2e6; padding: 8px;">Clases y funciones del Python activo</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Aprendizaje</td><td style="border: 1px solid #dee2e6; padding: 8px;">Accesos a Tutoriales, Debugger, Paquetes y Análisis (F4–F7)</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Terminal</td><td style="border: 1px solid #dee2e6; padding: 8px;">Enfoca el panel inferior en la pestaña Terminal</td></tr>
            <tr><td style="border: 1px solid #dee2e6; padding: 8px;">Settings</td><td style="border: 1px solid #dee2e6; padding: 8px;">Abre Preferencias</td></tr>
        </table>
        
        <h3 style="color: #8E44AD;">⬇️ Panel inferior</h3>
        <ul>
            <li><strong>Mostrar/ocultar:</strong> <code>Ctrl+`</code> o Vista → Panel inferior</li>
            <li><strong>Cerrar:</strong> botón <strong>✕</strong> en la cabecera del panel — el editor ocupa todo el alto</li>
            <li><strong>Pestañas:</strong> Terminal (salida y comandos), Problems (misma lista que en sidebar), ayuda contextual</li>
            <li><strong>Ejecutar código:</strong> <code>Ctrl+Enter</code> abre el panel y enfoca el Terminal si estaba cerrado</li>
        </ul>
        
        <h3 style="color: #8E44AD;">☕ Modo Café y Pomodoro</h3>
        <ul>
            <li><strong>Activar pausa manual:</strong> botón <strong>☕</strong> en la barra superior o <code>Ctrl+Alt+C</code></li>
            <li>Overlay con taza y mensaje; la UI se desbloquea al mover el ratón o pulsar una tecla</li>
            <li><strong>Pomodoro</strong> (Preferencias → ☕ Café): descansos automáticos cada X minutos</li>
            <li>Barra de estado: <code>☕ MM:SS</code> hasta el próximo descanso</li>
            <li>Durante el descanso: overlay con <code>Descanso: MM:SS</code></li>
        </ul>
        
        <h3 style="color: #8E44AD;">⌨️ Navegación rápida</h3>
        <ul>
            <li><strong>Quick Open:</strong> <code>Ctrl+P</code> — archivos recientes</li>
            <li><strong>Command Palette:</strong> <code>Ctrl+Shift+P</code></li>
            <li><strong>Explorador:</strong> <code>F3</code> mostrar/ocultar sidebar del explorador</li>
        </ul>
        
        <div style="background-color: #E8F6F3; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>💡 Consejo:</strong> Usa <strong>Outline</strong> en archivos largos y <strong>Problems</strong> mientras escribes para corregir la sintaxis antes de ejecutar.
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_terminal_tab(self):
        """Crea la pestaña del terminal"""
        content = """
        <h2 style="color: #2C3E50;">💻 Terminal Integrado</h2>
        
        <h3 style="color: #8E44AD;">🚀 Ejecutar desde el editor</h3>
        <p><code>Ctrl+Enter</code> o el botón <strong>🚀 Ejecutar Código</strong> lanza <strong>todo el programa</strong>, no línea a línea:</p>
        <ul>
            <li><strong>Archivo guardado:</strong> <code>cd carpeta && python archivo.py</code> en el shell integrado (Bash)</li>
            <li><strong>Sin guardar:</strong> se crea un <code>.py</code> temporal en la carpeta de trabajo y se ejecuta entero</li>
            <li><strong>Cambios sin guardar:</strong> se guarda automáticamente antes de ejecutar (si la pestaña tiene ruta)</li>
            <li><strong>Scripts interactivos</strong> (menús, <code>input()</code>, Rich…): escribe en la <strong>caja inferior</strong> del terminal y pulsa Enter</li>
            <li><strong>TUIs a pantalla completa</strong> (p. ej. Textual): mejor usar <code>Ctrl+Alt+T</code> (terminal del sistema)</li>
        </ul>
        
        <h3 style="color: #8E44AD;">🔄 Shell y caja de comandos</h3>
        <p>El desplegable del terminal permite elegir <strong>Python</strong>, <strong>Bash</strong>, Zsh, etc. La <strong>caja inferior</strong> envía comandos al shell activo.</p>
        <ul>
            <li><strong>Modo Limpio / Interactivo / Auto-detect:</strong> solo afectan a comandos que <em>tú</em> escribes a mano, no al botón Ejecutar del editor</li>
            <li><strong>Precapturar inputs:</strong> diálogo para rellenar <code>input()</code> antes de lanzar (scripts simples)</li>
            <li><strong>Limpiar / Reiniciar:</strong> botones en la barra del terminal</li>
        </ul>
        
        <h3 style="color: #8E44AD;">🔤 Ejemplos en la caja de comandos</h3>
        <h4>Con shell Python:</h4>
        <div style="background-color: #f8f9fa; padding: 10px; border-left: 4px solid #28a745; margin: 10px 0;">
            <code>print("¡Hola mundo!")</code><br>
            <code>x = 5 + 3</code>
        </div>
        
        <h4>Con shell Bash:</h4>
        <div style="background-color: #f8f9fa; padding: 10px; border-left: 4px solid #007bff; margin: 10px 0;">
            <code>ls -la</code><br>
            <code>pwd</code><br>
            <code>python3 mi_script.py</code>
        </div>
        
        <h3 style="color: #8E44AD;">⚙️ Controles del Terminal</h3>
        <ul>
            <li><strong>🗑️ Limpiar:</strong> Borra la salida visible</li>
            <li><strong>🔄 Reiniciar:</strong> Reinicia el shell</li>
            <li><strong>Cambiar Shell:</strong> Desplegable en la barra del terminal</li>
            <li><strong>🖥️ Terminal del Sistema:</strong> <code>Ctrl+Alt+T</code> — terminal nativa del SO (recomendada para proyectos con venv propio o TUI)</li>
        </ul>
        
        <div style="background-color: #FFF3CD; padding: 15px; border-radius: 5px; margin: 15px 0;">
            <strong>⚠️ Importante:</strong>
            <ul>
                <li>Los errores de <strong>ejecución</strong> aparecen aquí, no en Problems</li>
                <li>Abre la <strong>carpeta del proyecto</strong> (<code>Ctrl+Shift+O</code>) antes de ejecutar scripts que usan <code>__file__</code> o archivos relativos</li>
            </ul>
        </div>
        """
        return self.create_scrollable_content(content)
    
    def create_educational_tab(self):
        """Crea la pestaña de funciones educativas"""
        content = """
        <h2 style="color: #2C3E50;">🎓 Funciones de Aprendizaje</h2>
        
        <p>El editor incluye <strong>5 funcionalidades educativas especiales</strong> diseñadas para ayudar a principiantes a aprender Python de manera efectiva.</p>
        
        <h3 style="color: #8E44AD;">🧭 Acceso rápido (sidebar Aprendizaje)</h3>
        <p>En la <strong>Activity Bar</strong> → icono <strong>Aprendizaje</strong> tienes botones para abrir cada herramienta sin memorizar solo los atajos.</p>
        
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
        <p>Sugerencias mientras escribes en el editor (palabras clave, builtins, snippets). Complementa el panel <strong>Problems</strong>, que muestra errores de sintaxis tras una breve pausa al escribir.</p>
        <ul>
            <li>Palabras clave y funciones built-in con descripción breve</li>
            <li>Snippets comunes (<code>def</code>, <code>class</code>, <code>if</code>, …)</li>
            <li><code>Escape</code> cierra la lista; no confundir con Problems</li>
        </ul>
        
        <h3 style="color: #8E44AD;">📚 Tutoriales Interactivos (F4)</h3>
        <p>Aprende Python paso a paso con <strong>17 tutoriales</strong> ordenados del nivel básico al experto:</p>
        
        <h4>🟢 Principiante</h4>
        <ul>
            <li>Primeros pasos con Python · Strings y texto · Diccionarios · Estructuras de control</li>
        </ul>
        <h4>🟡 Intermedio</h4>
        <ul>
            <li>Listas y funciones · Tuplas y conjuntos · Archivos · Errores · Módulos · Comprensiones</li>
        </ul>
        <h4>🟠 Avanzado</h4>
        <ul>
            <li>POO · Herencia · Context managers · Generadores</li>
        </ul>
        <h4>🔴 Experto</h4>
        <ul>
            <li>Decoradores · Async/await · Type hints y dataclasses</li>
        </ul>
        <p>En el diálogo F4 los tutoriales aparecen agrupados por nivel; empieza por los de principiante.</p>
        
        <h3 style="color: #8E44AD;">🐛 Debugger Visual (F5)</h3>
        <p>Ejecuta tu código paso a paso para entender cómo funciona:</p>
        <ul>
            <li><strong>▶️ Ejecutar paso a paso</strong>: Ve línea por línea</li>
            <li><strong>📊 Inspección de variables</strong>: Ve valores en tiempo real</li>
            <li><strong>🚀 Ejecutar hasta breakpoint</strong>: Control de paradas</li>
            <li><strong>📤 Captura de salida</strong>: Ve qué imprime tu programa</li>
        </ul>
        
        <h3 style="color: #8E44AD;">📦 Gestor de Paquetes Visual (F6)</h3>
        <p>Instala y gestiona paquetes Python con un catálogo de <strong>más de 40 librerías</strong> habituales:</p>
        <ul>
            <li><strong>Web:</strong> requests, httpx, flask, django, fastapi, beautifulsoup4, selenium…</li>
            <li><strong>Datos y ciencia:</strong> pandas, numpy, scipy, scikit-learn, openpyxl</li>
            <li><strong>GUI y terminal:</strong> PySide6, rich, textual, customtkinter</li>
            <li><strong>Datos y persistencia:</strong> sqlalchemy (ORM), pymongo, psycopg2-binary (drivers/clientes)</li>
            <li><strong>Desarrollo:</strong> pytest, black, ruff, mypy, autopep8</li>
            <li>Filtro por categoría, ejemplos de código e instalación con un clic</li>
        </ul>
        
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
            <li><strong>Progresión estructurada:</strong> 17 tutoriales del nivel principiante al experto</li>
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
            <li><strong>Mostrar/Ocultar:</strong> <code>F3</code> o Activity Bar → Explorer</li>
            <li><strong>Abrir carpeta de trabajo:</strong> <code>Ctrl+Shift+O</code> — la ruta aparece en la barra superior</li>
            <li><strong>Iconos por tipo:</strong> Python, Markdown, JSON, imágenes, etc.</li>
            <li><strong>Abrir archivo:</strong> Doble clic (sin ventanas de confirmación)</li>
            <li><strong>Primer archivo:</strong> reutiliza la pestaña vacía «Nuevo 1» si sigue sin contenido</li>
        </ul>
        
        <h3 style="color: #F39C12;">⚠️ Problems y 📋 Outline</h3>
        <ul>
            <li><strong>Problems:</strong> sidebar + panel inferior; badge en Activity Bar</li>
            <li><strong>Outline:</strong> navegación por símbolos del <code>.py</code> activo</li>
            <li>Ver pestañas <strong>📝 Editor</strong> e <strong>🖥️ Interfaz</strong> para más detalle</li>
        </ul>
        
        <h3 style="color: #F39C12;">☕ Modo Café y Pomodoro</h3>
        <ul>
            <li>Botón <strong>☕</strong> o <code>Ctrl+Alt+C</code></li>
            <li>Configuración en Preferencias → pestaña <strong>☕ Café</strong></li>
            <li>Pomodoro: intervalo de trabajo, duración del descanso y mensaje personalizado</li>
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
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Enter</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Ejecutar programa completo en terminal (solo .py)</td>
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
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + N</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Nueva pestaña vacía</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + T</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Nueva pestaña (alternativo)</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + O</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir archivo</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + O</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir carpeta de trabajo</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + S</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Guardar archivo</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + S</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Guardar como</td>
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
                <td style="border: 1px solid #dee2e6; padding: 8px;">Siguiente coincidencia (diálogo buscar) / mostrar explorador</td>
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
                <td style="border: 1px solid #dee2e6; padding: 8px;">Mostrar/ocultar explorador (sidebar)</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + `</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Mostrar/ocultar panel inferior</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + V</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Vista previa Markdown (solo .md)</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + P</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Quick Open (archivos recientes)</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Shift + P</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Command Palette</td>
            </tr>
            <tr style="background-color: #f8f9fa;">
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Alt + T</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Abrir terminal del sistema operativo</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dee2e6; padding: 8px;"><code>Ctrl + Alt + C</code></td>
                <td style="border: 1px solid #dee2e6; padding: 8px;">Modo Café (pausa manual)</td>
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
