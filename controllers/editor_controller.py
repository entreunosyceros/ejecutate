"""
Controlador: Maneja la lógica de interacción entre Vista y Modelo
Versión PySide6 con resaltado de sintaxis
"""
from models.code_executor import CodeExecutor
from views.editor_view import CodeEditorViewPySide
from config import AppConfig


class CodeEditorController:
    """Controlador principal del editor de código con PySide6"""
    
    def __init__(self):
        self.model = CodeExecutor()
        self.view = CodeEditorViewPySide()
        self._setup_bindings()
    
    def _setup_bindings(self):
        """Configura los eventos y comandos de la vista"""
        # Asociar comandos a los botones
        self.view.set_button_command("execute_terminal", self.execute_code_in_terminal)
        self.view.set_button_command("clear", self.clear_all)
        
        # Asociar comandos del menú
        self.view.set_menu_commands(
            self.open_file,
            self.save_file,
            self.save_file_as,
            self.exit_application,
            self.show_preferences,
            self.show_about
        )
        
        # Ctrl+Enter ejecuta en terminal integrado (no usar exec() en el hilo GUI)
        self.view.set_key_bindings(self.execute_code_in_terminal, self.clear_all)
    
    def execute_code(self):
        """Ejecuta el código ingresado por el usuario"""
        code = self.view.get_input_code()
        
        if not code:
            self.view.show_message(
                "Advertencia", 
                AppConfig.EMPTY_CODE_WARNING,
                "warning"
            )
            return
        
        try:
            # Limpiar salida anterior
            self.view.clear_output()
            
            # Ejecutar código usando el modelo
            result = self.model.execute_code(code)
            
            # Mostrar resultados en la vista
            if result['output']:
                self.view.append_output(result['output'])
            
            if result['errors']:
                if result['output']:
                    self.view.append_output("\n" + "="*50 + "\n")
                self.view.append_output("ERRORES:\n", is_error=True)
                self.view.append_output(result['errors'], is_error=True)
            
            if not result['output'] and not result['errors']:
                self.view.set_output(AppConfig.SUCCESS_MESSAGE)
                
        except Exception as e:
            self.view.show_message(
                "Error del Sistema", 
                f"Error inesperado: {str(e)}",
                "error"
            )
    
    def execute_code_in_terminal(self):
        """Ejecuta el código en el terminal integrado"""
        try:
            self.view.execute_code_in_terminal()
        except Exception as e:
            self.view.show_message(
                "Error del Sistema", 
                f"Error ejecutando en terminal: {str(e)}",
                "error"
            )
    
    def clear_all(self):
        """Limpia tanto el código de entrada como la salida"""
        self.view.clear_input()
        self.view.clear_output()
    
    def clear_output_only(self):
        """Limpia solo el área de salida"""
        self.view.clear_output()
    
    def open_file(self):
        """Abre un archivo Python"""
        # Verificar si hay cambios sin guardar
        if self.view.has_unsaved_changes():
            reply = self.view.show_confirmation(
                "Cambios sin guardar",
                "Hay cambios sin guardar. ¿Desea continuar sin guardar?"
            )
            if not reply:
                return
        
        file_path = self.view.open_file_dialog()
        if file_path:
            success = self.view.load_file_content(file_path)
            if success:
                self.view.clear_output()
                self.view.set_output(f"✅ Archivo cargado: {file_path}")
    
    def save_file(self):
        """Guarda el archivo actual"""
        current_path = self.view.get_current_file_path()
        if current_path:
            success = self.view.save_file_content()
            if success:
                self.view.show_message("Éxito", "Archivo guardado correctamente", "info")
        else:
            # Si no hay archivo actual, abrir diálogo "Guardar como"
            self.save_file_as()
    
    def save_file_as(self):
        """Guarda el archivo con un nuevo nombre"""
        file_path = self.view.save_file_dialog()
        if file_path:
            # Asegurar que el archivo tenga extensión .py
            if not file_path.endswith('.py'):
                file_path += '.py'
            
            success = self.view.save_file_content(file_path)
            if success:
                self.view.show_message("Éxito", f"Archivo guardado como: {file_path}", "info")
    
    def exit_application(self):
        """Sale de la aplicación"""
        # Verificar si hay cambios sin guardar
        if self.view.has_unsaved_changes():
            reply = self.view.show_confirmation(
                "Salir",
                "Hay cambios sin guardar. ¿Está seguro de que desea salir?"
            )
            if not reply:
                return
        
        # Cerrar la aplicación completamente (no minimizar a bandeja)
        self.view._quit_application()
    
    def show_about(self):
        """Muestra la ventana About"""
        self.view.show_about_dialog()
    
    def show_preferences(self):
        """Muestra la ventana de preferencias"""
        self.view.show_preferences_dialog()
    
    def run(self):
        """Inicia la aplicación"""
        try:
            # Mostrar mensaje de bienvenida
            welcome_msg = AppConfig.WELCOME_MESSAGE + "\n\n🎨 ¡Resaltado de sintaxis activado con PySide6!"
            self.view.set_output(welcome_msg)
            
            # Iniciar el bucle principal de PySide6
            return self.view.run()
            
        except KeyboardInterrupt:
            print("\n¡Aplicación cerrada por el usuario!")
            return 0
        except Exception as e:
            print(f"Error fatal en controlador: {e}")
            return 1
        finally:
            # Limpieza final
            try:
                if hasattr(self, 'view') and self.view:
                    # Limpiar recursos antes de destruir
                    if hasattr(self.view, '_cleanup_resources'):
                        self.view._cleanup_resources()
                    self.view.destroy()
            except:
                pass
