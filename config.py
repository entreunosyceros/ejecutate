"""
Configuraciones de la aplicación
"""

class AppConfig:
    """Configuraciones generales de la aplicación"""
    
    # Configuración de la ventana principal
    WINDOW_TITLE = "Ejecútalo! - Editor básico de Python"
    WINDOW_GEOMETRY = "1000x700"
    
    # Configuración del área de código
    CODE_AREA_HEIGHT = 15
    CODE_AREA_WIDTH = 80
    CODE_FONT = ("Consolas", 12)
    
    # Configuración del área de salida
    OUTPUT_AREA_HEIGHT = 10
    OUTPUT_AREA_WIDTH = 80
    OUTPUT_FONT = ("Consolas", 11)
    
    # Configuración de indentación
    INDENT_SIZE = 4  # Espacios por nivel de indentación
    AUTO_INDENT = True  # Activar indentación automática
    
    # Configuración de colores
    EXECUTE_BUTTON_COLOR = "#27AE60"
    CLEAR_BUTTON_COLOR = "#E74C3C"
    ERROR_TEXT_COLOR = "#C0392B"
    
    # Configuración de bandeja del sistema
    TRAY_ENABLED = True
    TRAY_ICON_PATH = "img/logo.png"
    TRAY_TOOLTIP = "Editor de Código Python"
    
    # Configuración de preferencias
    PREFERENCES_ENABLED = True
    AUTO_SAVE_PREFERENCES = True
    
    # Configuración del explorador de archivos
    FILE_EXPLORER_ENABLED = True
    FILE_EXPLORER_WIDTH = 250
    FILE_EXPLORER_SHOW_HIDDEN = False
    FILE_EXPLORER_AUTO_EXPAND = True
    SUPPORTED_EXTENSIONS = ['.py', '.txt', '.md', '.json', '.yaml', '.yml', '.ini', '.cfg']
    
    # Configuración de pestañas
    TABS_ENABLED = True
    TABS_MAX_COUNT = 10
    TABS_SHOW_CLOSE_BUTTON = True
    TABS_CONFIRM_CLOSE_UNSAVED = True
    
    # Configuración de temas múltiples
    THEMES_ENABLED = True
    DEFAULT_THEME = "Oscuro"

    # Tipografía UI (separada del editor)
    UI_FONT_FAMILY = "Inter"
    UI_FONT_SIZE = 13
    
    # Configuración del terminal integrado
    TERMINAL_ENABLED = True
    TERMINAL_SHOW_IN_TABS = True
    TERMINAL_PYTHON_REPL = True
    TERMINAL_SYSTEM_COMMANDS = True
    TERMINAL_PIP_INTEGRATION = True
    TERMINAL_HISTORY_SIZE = 1000
    TERMINAL_AUTO_SCROLL = True
    TERMINAL_FONT_FAMILY = "Consolas"
    TERMINAL_FONT_SIZE = 11
    
    # Configuración de gestión de sesiones
    SESSION_MANAGEMENT_ENABLED = True
    SESSION_AUTO_SAVE = True
    SESSION_RESTORE_ON_STARTUP = True
    SESSION_SAVE_UNSAVED_FILES = True
    SESSION_REMEMBER_WINDOW_STATE = True
    SESSION_REMEMBER_THEME = True
    SESSION_FILE_PATH = ".editor_session.json"
    SESSION_MAX_RECENT_FILES = 10
    
    # Configuración de formatter automático
    FORMATTER_ENABLED = True
    FORMATTER_AUTO_FORMAT_ON_SAVE = False  # Usuario puede habilitar/deshabilitar
    FORMATTER_PEP8_COMPLIANCE = True
    FORMATTER_AUTO_SPACING = True
    FORMATTER_ORGANIZE_IMPORTS = True
    FORMATTER_MAX_LINE_LENGTH = 88  # PEP 8 recomienda 79, pero Black usa 88
    FORMATTER_INDENT_SIZE = 4
    FORMATTER_USE_TABS = False
    FORMATTER_REMOVE_TRAILING_WHITESPACE = True
    FORMATTER_ADD_FINAL_NEWLINE = True
    FORMATTER_SORT_IMPORTS_GROUPS = True  # Separar stdlib, third-party, local
    FORMATTER_ENGINE = "autopep8"  # autopep8, black, o manual

    # Modo Café / Pomodoro
    COFFEE_MESSAGE = "Mueve el ratón o pulsa cualquier tecla para volver."
    COFFEE_POMODORO_ENABLED = False
    COFFEE_POMODORO_WORK_MINUTES = 25
    COFFEE_POMODORO_BREAK_MINUTES = 5
    
    # Configuración de búsqueda y reemplazo
    SEARCH_ENABLED = True
    SEARCH_CASE_SENSITIVE = False
    SEARCH_WHOLE_WORDS = False
    SEARCH_REGEX_ENABLED = True
    SEARCH_HIGHLIGHT_ALL = True
    SEARCH_WRAP_AROUND = True
    SEARCH_IN_SELECTION = False
    SEARCH_HISTORY_SIZE = 20
    REPLACE_HISTORY_SIZE = 20
    SEARCH_MULTI_FILE_ENABLED = True
    SEARCH_FILE_PATTERNS = ["*.py", "*.txt", "*.md", "*.json", "*.yaml", "*.yml"]
    SEARCH_EXCLUDE_PATTERNS = ["*.pyc", "__pycache__", ".git", ".venv", "node_modules"]
    
    # Definición de temas predefinidos
    THEMES = {
        "Oscuro": {
            # Editor
            'editor_bg_color': '#2C3E50',
            'editor_text_color': '#ECF0F1',
            'editor_selection_color': '#3498DB',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,
            
            # Numeración de líneas
            'line_number_bg_color': '#34495E',
            'line_number_text_color': '#BDC3C7',
            
            # Área de salida
            'output_bg_color': '#2C3E50',
            'output_text_color': '#ECF0F1',
            'output_font_family': 'Consolas',
            'output_font_size': 11,
            
            # Resaltado de sintaxis
            'syntax_keyword_color': '#FF6B35',
            'syntax_string_color': '#2ECC71',
            'syntax_comment_color': '#95A5A6',
            'syntax_number_color': '#E74C3C',
            'syntax_operator_color': '#9B59B6',
            'syntax_builtin_color': '#3498DB',
            'syntax_function_color': '#F39C12',
            'syntax_class_color': '#E67E22'
        },
        
        "Claro": {
            # Editor
            'editor_bg_color': '#FFFFFF',
            'editor_text_color': '#2C3E50',
            'editor_selection_color': '#3498DB',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,
            
            # Numeración de líneas
            'line_number_bg_color': '#F8F9FA',
            'line_number_text_color': '#6C757D',
            
            # Área de salida
            'output_bg_color': '#FFFFFF',
            'output_text_color': '#2C3E50',
            'output_font_family': 'Consolas',
            'output_font_size': 11,
            
            # Resaltado de sintaxis
            'syntax_keyword_color': '#0000FF',
            'syntax_string_color': '#008000',
            'syntax_comment_color': '#808080',
            'syntax_number_color': '#FF0000',
            'syntax_operator_color': '#800080',
            'syntax_builtin_color': '#0066CC',
            'syntax_function_color': '#FF8C00',
            'syntax_class_color': '#8B4513'
        },
        
        "Solarized": {
            # Editor
            'editor_bg_color': '#002B36',
            'editor_text_color': '#839496',
            'editor_selection_color': '#268BD2',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,
            
            # Numeración de líneas
            'line_number_bg_color': '#073642',
            'line_number_text_color': '#586E75',
            
            # Área de salida
            'output_bg_color': '#002B36',
            'output_text_color': '#839496',
            'output_font_family': 'Consolas',
            'output_font_size': 11,
            
            # Resaltado de sintaxis
            'syntax_keyword_color': '#859900',
            'syntax_string_color': '#2AA198',
            'syntax_comment_color': '#586E75',
            'syntax_number_color': '#DC322F',
            'syntax_operator_color': '#D33682',
            'syntax_builtin_color': '#268BD2',
            'syntax_function_color': '#B58900',
            'syntax_class_color': '#CB4B16'
        },
        
        "Monokai": {
            # Editor
            'editor_bg_color': '#272822',
            'editor_text_color': '#F8F8F2',
            'editor_selection_color': '#49483E',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,
            
            # Numeración de líneas
            'line_number_bg_color': '#3E3D32',
            'line_number_text_color': '#90908A',
            
            # Área de salida
            'output_bg_color': '#272822',
            'output_text_color': '#F8F8F2',
            'output_font_family': 'Consolas',
            'output_font_size': 11,
            
            # Resaltado de sintaxis
            'syntax_keyword_color': '#F92672',
            'syntax_string_color': '#E6DB74',
            'syntax_comment_color': '#75715E',
            'syntax_number_color': '#AE81FF',
            'syntax_operator_color': '#F92672',
            'syntax_builtin_color': '#66D9EF',
            'syntax_function_color': '#A6E22E',
            'syntax_class_color': '#A6E22E'
        },
        
        "VS Code Dark": {
            # Editor
            'editor_bg_color': '#1E1E1E',
            'editor_text_color': '#D4D4D4',
            'editor_selection_color': '#264F78',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,
            
            # Numeración de líneas
            'line_number_bg_color': '#252526',
            'line_number_text_color': '#858585',
            
            # Área de salida
            'output_bg_color': '#1E1E1E',
            'output_text_color': '#D4D4D4',
            'output_font_family': 'Consolas',
            'output_font_size': 11,
            
            # Resaltado de sintaxis
            'syntax_keyword_color': '#569CD6',
            'syntax_string_color': '#CE9178',
            'syntax_comment_color': '#6A9955',
            'syntax_number_color': '#B5CEA8',
            'syntax_operator_color': '#D4D4D4',
            'syntax_builtin_color': '#4EC9B0',
            'syntax_function_color': '#DCDCAA',
            'syntax_class_color': '#4EC9B0'
        }
        ,
        "Café": {
            # Editor
            'editor_bg_color': '#2B1B12',
            'editor_text_color': '#F3E7DA',
            'editor_selection_color': '#5C3A25',
            'editor_font_family': 'Consolas',
            'editor_font_size': 12,

            # Numeración de líneas
            'line_number_bg_color': '#23160F',
            'line_number_text_color': '#CDB8A6',

            # Área de salida
            'output_bg_color': '#2B1B12',
            'output_text_color': '#F3E7DA',
            'output_font_family': 'Consolas',
            'output_font_size': 11,

            # Resaltado de sintaxis (cálido)
            'syntax_keyword_color': '#D69A5A',
            'syntax_string_color': '#CFAF8A',
            'syntax_comment_color': '#A08978',
            'syntax_number_color': '#E2B07A',
            'syntax_operator_color': '#F3E7DA',
            'syntax_builtin_color': '#B38B5D',
            'syntax_function_color': '#E2B07A',
            'syntax_class_color': '#D69A5A'
        }
    }
    
    # Mensajes
    WELCOME_MESSAGE = """
🐍 ¡Bienvenido al Editor de Código Python Profesional!

🚀 Nuevas Características:
• 🎭 Bandeja del sistema: Minimiza a la bandeja al cerrar
• ⚙️ Preferencias persistentes: Se guardan automáticamente
• 🎨 Temas personalizables: Colores, fuentes y tamaños
• 📏 Numeración de líneas con colores personalizables
• 🔧 Indentación automática avanzada (reconoce contexto)
• 🤖 Autocompletado inteligente con snippets y documentación
• 📁 Explorador de archivos lateral navegable
• 🔧 Formatter automático: PEP 8, autopep8, black

📁 Gestión de Archivos:
• Ctrl+O: Abrir archivo Python
• Ctrl+S: Guardar archivo actual
• Ctrl+Shift+S: Guardar como nuevo archivo
• Ctrl+Q: Salir (minimiza a bandeja)
• F3: Alternar explorador de archivos

📂 Gestión de Pestañas:
• Ctrl+T: Nueva pestaña
• Ctrl+W: Cerrar pestaña actual
• 🔄 Doble clic: Abrir archivo en nueva pestaña
• • Indicador de archivos modificados
• ⚠️ Confirmación antes de cerrar pestañas modificadas
• 🏷️ Nombres de archivo en pestañas
• 📝 Múltiples archivos abiertos simultáneamente

🗂️ Explorador de Archivos:
• 🌳 Árbol de directorios navegable
• 📄 Apertura rápida con doble clic
• ➕ Crear archivos/carpetas (clic derecho)
• 🗑️ Eliminar archivos/carpetas
• 📂 Gestión completa de proyectos
• 🔍 Filtrado por extensiones soportadas

🎨 Personalización:
• Ctrl+,: Abrir preferencias completas
• 👁️ Vista previa en tiempo real
• 🔄 Restablecer a valores por defecto
• 💾 Guardado automático de configuración

⌨️ Atajos de Edición:
• Ctrl+Enter: Ejecutar código
• Ctrl+L: Limpiar todo
• Ctrl+Shift+F: Formatear código (PEP 8)
• Tab: Indentar línea/selección
• Shift+Tab: Des-indentar línea/selección
• F1: Información y ayuda

💻 Terminal Integrado:
• 🐍 REPL Python interactivo
• 📦 Instalación de paquetes con pip
• ⚡ Comandos del sistema (ls, cd, etc.)
• 📊 Historial de comandos
• 🔄 Autocompletado de comandos
• Ctrl+`: Alternar terminal

💾 Gestión de Sesiones:
• 🔄 Restauración automática de archivos
• 💭 Recordar posición del cursor
• 🎨 Persistencia de tema seleccionado
• 📋 Historial de archivos recientes
• 💾 Guardado automático de sesión
• 🪟 Restaurar estado de ventana

🤖 Autocompletado:
• Automático después de 1 carácter
• ⬆️⬇️: Navegar sugerencias
• Enter/Tab: Insertar sugerencia
• Escape: Cerrar autocompletado

🔔 Bandeja del Sistema:
• Cerrar ventana: Minimiza a bandeja
• Doble clic en icono: Restaurar ventana
• Clic derecho: Menú con opciones
• Menú → Salir: Cierra completamente

¡Configura tu editor ideal y Ejecútate! 🐍✨
    """.strip()
    
    EMPTY_CODE_WARNING = "Por favor, ingresa algún código para ejecutar."
    SUCCESS_MESSAGE = "✅ Código ejecutado correctamente (sin salida)"
