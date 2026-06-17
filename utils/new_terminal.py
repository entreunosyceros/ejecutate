#!/usr/bin/env python3
"""
Terminal integrado real usando QProcess
Este archivo contiene la nueva implementación del terminal
"""

import time
import os
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
                               QLineEdit, QPushButton, QLabel, QComboBox, QInputDialog, QCheckBox,
                               QDialog, QFormLayout)
from PySide6.QtCore import Qt, QProcess, QProcessEnvironment, QTimer, QSettings
from PySide6.QtGui import QFont, QColor
import sys

class IntegratedTerminalNew(QWidget):
    """Terminal integrado real del sistema usando QProcess"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_editor = parent
        self.process = None
        self.command_history = []
        self.history_index = -1
        self.current_command = ""
        self.command_finished = True
        self.setup_ui()
        self.start_terminal()

    def setup_ui(self):
        """Configura la interfaz del terminal (versión corregida)"""
        layout = QVBoxLayout()
        toolbar = QHBoxLayout()

        # Intérprete
        self.shell_combo = QComboBox()
        py_exec = sys.executable or 'python'
        # Intentar detectar venv explícito
        venv_path = os.environ.get('VIRTUAL_ENV')
        py_label = "🐍 Python (venv)" if venv_path else "🐍 Python"
        for text, data in [
            (py_label, py_exec),
            ("🐧 Bash", "/bin/bash"),
            ("🐚 Zsh", "/bin/zsh"),
            ("🐟 Fish", "/usr/bin/fish"),
            ("📱 Sh", "/bin/sh")
        ]:
            self.shell_combo.addItem(text, data)
        self.shell_combo.currentTextChanged.connect(self.change_shell)

        # Botones básicos
        self.clear_btn = QPushButton("🗑️ Limpiar")
        self.clear_btn.setMaximumWidth(80)
        self.clear_btn.setStyleSheet("""
            QPushButton { background:#E74C3C; color:#fff; border:none; padding:5px 10px; border-radius:3px; }
            QPushButton:hover { background:#C0392B; }
        """)
        self.clear_btn.clicked.connect(self.clear_terminal)

        self.restart_btn = QPushButton("🔄 Reiniciar")
        self.restart_btn.setMaximumWidth(90)
        self.restart_btn.setStyleSheet("""
            QPushButton { background:#3498DB; color:#fff; border:none; padding:5px 10px; border-radius:3px; }
            QPushButton:hover { background:#2980B9; }
        """)
        self.restart_btn.clicked.connect(self.restart_terminal)

        # Modo ejecución
        self.exec_mode_combo = QComboBox()
        self.exec_mode_combo.addItem("⚡ Limpio", "clean")
        self.exec_mode_combo.addItem("🧪 Interactivo", "interactive")

        # Auto-detect persistente
        self.auto_detect_checkbox = QCheckBox("🧠 Auto-detect")
        try:
            settings = QSettings("Ejecutate", "EditorPython")
            self.auto_detect_checkbox.setChecked(settings.value("terminal/auto_detect", True, type=bool))
        except Exception:
            self.auto_detect_checkbox.setChecked(True)
        self.auto_detect_checkbox.setToolTip("Detectar automáticamente código interactivo (input) y cambiar al modo adecuado")
        self.auto_detect_checkbox.stateChanged.connect(self._persist_auto_detect)

        # Precaptura
        self.precapture_checkbox = QCheckBox("📝 Precapturar inputs")
        # Cargar preferencia persistida (por defecto True)
        try:
            settings = QSettings("Ejecutate", "EditorPython")
            self.precapture_checkbox.setChecked(settings.value("terminal/precapture", True, type=bool))
        except Exception:
            self.precapture_checkbox.setChecked(True)
        self.precapture_checkbox.setToolTip("Recolectar valores para input() antes de ejecutar y simularlos en modo limpio")
        self.precapture_checkbox.stateChanged.connect(self._persist_precapture)
        # Construcción toolbar con estilos dentro del método
        label_interp = QLabel("🖥️ Intérprete:")
        label_mode = QLabel("⚙️ Modo:")
        common_label_style = "color:#FFFFFF; font-weight:bold;"
        label_interp.setStyleSheet(common_label_style)
        label_mode.setStyleSheet(common_label_style)
        self.auto_detect_checkbox.setStyleSheet("color:#FFFFFF;")
        self.precapture_checkbox.setStyleSheet("color:#FFFFFF;")

        toolbar.addWidget(label_interp)
        toolbar.addWidget(self.shell_combo)
        toolbar.addWidget(label_mode)
        toolbar.addWidget(self.exec_mode_combo)
        toolbar.addWidget(self.auto_detect_checkbox)
        toolbar.addWidget(self.precapture_checkbox)
        toolbar.addStretch()
        toolbar.addWidget(self.clear_btn)
        toolbar.addWidget(self.restart_btn)

        from PySide6.QtWidgets import QWidget as _QW
        toolbar_container = _QW()
        toolbar_container.setLayout(toolbar)
        toolbar_container.setStyleSheet("background:#2B2B2B; border:1px solid #444; padding:4px 6px;")

        # Salida terminal
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setFont(QFont("Consolas", 11))
        self.terminal_output.setStyleSheet("QTextEdit { background:#1E1E1E; color:#FFFFFF; border:1px solid #444; }")

        # Entrada comandos
        self.command_input = QLineEdit()
        self.command_input.setFont(QFont("Consolas", 11))
        self.command_input.setStyleSheet("""
            QLineEdit { background:#2D2D2D; color:#FFFFFF; border:1px solid #444; padding:8px; border-radius:3px; }
            QLineEdit:focus { border:2px solid #3498DB; }
        """)
        self.command_input.setPlaceholderText("Escribe tu comando aquí y presiona Enter...")
        self.command_input.returnPressed.connect(self.execute_command)
        self.command_input.keyPressEvent = self.handle_key_press

        self.execute_btn = QPushButton("▶️ Ejecutar")
        self.execute_btn.setStyleSheet("""
            QPushButton { background:#27AE60; color:#fff; border:none; padding:8px 15px; border-radius:3px; }
            QPushButton:hover { background:#2ECC71; }
        """)
        self.execute_btn.clicked.connect(self.execute_command)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.command_input)
        input_layout.addWidget(self.execute_btn)

        self.status_label = QLabel("🔴 Terminal detenido")
        self.status_label.setStyleSheet("color:#E74C3C; font-weight:bold;")

        layout.addWidget(toolbar_container)
        layout.addWidget(self.terminal_output)
        layout.addLayout(input_layout)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def _stop_process(self, wait_ms: int = 3000):
        """Detiene el QProcess del shell si sigue en ejecución."""
        proc = self.process
        if not proc:
            return
        try:
            if proc.state() == QProcess.ProcessState.Running:
                proc.terminate()
                if not proc.waitForFinished(wait_ms):
                    proc.kill()
                    proc.waitForFinished(1000)
        except Exception:
            pass

    def shutdown_terminal(self, wait_ms: int = 2000):
        """Cierra el shell de forma segura antes de destruir el widget."""
        proc = self.process
        if not proc:
            return
        self.process = None
        try:
            proc.blockSignals(True)
        except Exception:
            pass
        try:
            if proc.state() == QProcess.ProcessState.Running:
                proc.kill()
                proc.waitForFinished(wait_ms)
        except Exception:
            pass

    def closeEvent(self, event):
        self.shutdown_terminal()
        super().closeEvent(event)

    def start_terminal(self):
        """Inicia el proceso del terminal"""
        try:
            if self.process:
                self._stop_process()
            self.process = QProcess(self)
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.finished.connect(self.handle_finished)
            self.process.started.connect(self.handle_started)
            
            self.change_shell()
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error al inicializar terminal: {str(e)}")

    def change_shell(self):
        """Cambia el shell del terminal"""
        try:
            self._stop_process()
            
            shell_data = self.shell_combo.currentData()
            
            if shell_data == sys.executable or shell_data.endswith('python') or shell_data.endswith('python3'):
                self.process.start(shell_data, ["-i", "-u"])
            else:
                self.process.start(shell_data, ["-i"])
            
            # Configurar el entorno del proceso
            env = QProcessEnvironment.systemEnvironment()
            env.insert("PYTHONUNBUFFERED", "1")
            env.insert("PYTHONIOENCODING", "utf-8")
            
            # Variables específicas para diferentes shells
            if shell_data == "/bin/bash":
                env.insert("PS1", "\\u@\\h:\\w$ ")
            elif shell_data == "/bin/zsh":
                env.insert("PS1", "%n@%m:%~ %# ")
            
            # Configurar variables básicas de terminal
            env.insert("TERM", "xterm-256color")
            env.insert("COLUMNS", "80")
            env.insert("LINES", "24")
            
            self.process.setProcessEnvironment(env)
            
            # Limpiar salida y mostrar información inicial
            self.terminal_output.clear()
            shell_name = self.shell_combo.currentText()
            self.terminal_output.append(f"🚀 Iniciando {shell_name}...")
            self.terminal_output.append("=" * 50)
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error al cambiar shell: {str(e)}")
    
    def execute_command(self):
        """Ejecuta un comando en el terminal"""
        try:
            command = self.command_input.text().strip()
            if not command:
                return
            
            # Agregar comando al historial
            if command not in self.command_history:
                self.command_history.append(command)
            self.history_index = len(self.command_history)
            
            # Mostrar comando en salida
            current_shell = self.shell_combo.currentText()
            self.terminal_output.append(f"\n📝 {current_shell} > {command}")
            
            # Verificar si el proceso está ejecutándose
            if not self.process or self.process.state() != QProcess.ProcessState.Running:
                self.terminal_output.append("❌ Terminal no está ejecutándose. Reiniciando...")
                self.start_terminal()
                return
            
            # Escribir comando al proceso
            command_bytes = (command + "\n").encode('utf-8')
            self.process.write(command_bytes)
            
            # Limpiar campo de entrada
            self.command_input.clear()
            
            # Marcar que hay un comando en ejecución
            self.current_command = command
            self.command_finished = False
            
            # Actualizar estado
            self.status_label.setText("⚡ Ejecutando comando...")
            self.status_label.setStyleSheet("color: #F39C12; font-weight: bold;")
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error ejecutando comando: {str(e)}")
    
    def handle_stdout(self):
        """Maneja la salida estándar del proceso"""
        try:
            data = self.process.readAllStandardOutput()
            text = data.data().decode('utf-8', errors='replace')
            
            if text.strip():
                # Configurar color verde para salida normal
                self.terminal_output.setTextColor(QColor("#00FF00"))
                self.terminal_output.insertPlainText(text)
                self.terminal_output.setTextColor(QColor("#FFFFFF"))  # Resetear color
                
                # Auto-scroll hacia abajo
                scrollbar = self.terminal_output.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
                
        except Exception as e:
            self.terminal_output.append(f"❌ Error procesando salida: {str(e)}")
    
    def handle_stderr(self):
        """Maneja la salida de error del proceso"""
        try:
            data = self.process.readAllStandardError()
            text = data.data().decode('utf-8', errors='replace')
            
            if text.strip():
                # Configurar color rojo para errores
                self.terminal_output.setTextColor(QColor("#FF4444"))
                self.terminal_output.insertPlainText(text)
                self.terminal_output.setTextColor(QColor("#FFFFFF"))  # Resetear color
                
                # Auto-scroll hacia abajo
                scrollbar = self.terminal_output.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
                
        except Exception as e:
            self.terminal_output.append(f"❌ Error procesando error: {str(e)}")
    
    def handle_started(self):
        """Maneja cuando el proceso se inicia exitosamente"""
        try:
            self.status_label.setText("🟢 Terminal ejecutándose")
            self.status_label.setStyleSheet("color: #27AE60; font-weight: bold;")

            shell_data = self.shell_combo.currentData()
            if shell_data == sys.executable or (isinstance(shell_data, str) and shell_data.endswith('python')):
                init_commands = [
                    "import sys",
                    "sys.ps1 = '🐍 >>> '",
                    "sys.ps2 = '🐍 ... '",
                    "print('🐍 Python interactivo listo!')"
                ]
                for cmd in init_commands:
                    self.process.write((cmd + "\n").encode('utf-8'))
            else:
                self.process.write("echo '🐧 Terminal listo!'\n".encode('utf-8'))
        except Exception as e:
            self.terminal_output.append(f"❌ Error inicializando shell: {e}")
    
    def handle_finished(self, exit_code):
        """Maneja cuando el proceso termina"""
        self.status_label.setText(f"🔴 Terminal terminado (código: {exit_code})")
        self.status_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
        
        if exit_code != 0:
            self.terminal_output.append(f"\n❌ Proceso terminado con código de error: {exit_code}")
        else:
            self.terminal_output.append(f"\n✅ Proceso terminado exitosamente")
    
    def clear_terminal(self):
        """Limpia la salida del terminal"""
        self.terminal_output.clear()
        self.terminal_output.append("🗑️ Terminal limpiado")
        self.terminal_output.append("=" * 30)
    
    def restart_terminal(self):
        """Reinicia el terminal"""
        try:
            self._stop_process()
            
            self.terminal_output.append("\n🔄 Reiniciando terminal...")
            self.terminal_output.append("=" * 40)
            
            # Pequeño delay para asegurar limpieza
            QTimer.singleShot(500, self.start_terminal)
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error reiniciando terminal: {str(e)}")
    
    def handle_key_press(self, event):
        """Maneja las teclas presionadas en el campo de entrada"""
        # Llamar al método original primero
        QLineEdit.keyPressEvent(self.command_input, event)
        
        # Manejar historial con flechas arriba/abajo
        if event.key() == Qt.Key_Up:
            if self.command_history and self.history_index > 0:
                self.history_index -= 1
                self.command_input.setText(self.command_history[self.history_index])
        elif event.key() == Qt.Key_Down:
            if self.command_history and self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.command_input.setText(self.command_history[self.history_index])
            elif self.history_index >= len(self.command_history) - 1:
                self.history_index = len(self.command_history)
                self.command_input.clear()
    
    def send_to_terminal(self, text):
        """Método público para enviar texto al terminal desde el editor"""
        try:
            if not self.process or self.process.state() != QProcess.ProcessState.Running:
                self.terminal_output.append("❌ Terminal no está ejecutándose. Iniciando...")
                self.start_terminal()
                return False
            
            # Mostrar el texto que se va a ejecutar
            self.terminal_output.append(f"\n📤 Enviando código al terminal:")
            self.terminal_output.append("─" * 40)
            self.terminal_output.setTextColor(QColor("#87CEEB"))
            self.terminal_output.insertPlainText(text)
            self.terminal_output.setTextColor(QColor("#FFFFFF"))
            self.terminal_output.append("─" * 40)
            
            # Verificar si necesitamos cambiar a Python
            if self.shell_combo.currentData() != sys.executable:
                self.shell_combo.setCurrentIndex(0)
                self.change_shell()
                # Esperar un poco para que se inicie Python
                QTimer.singleShot(1000, lambda: self._send_text_to_process(text))
            else:
                self._send_text_to_process(text)
            
            return True
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error enviando al terminal: {str(e)}")
            return False
    
    def _send_text_to_process(self, text):
        """Envía texto al proceso del terminal"""
        try:
            # Dividir en líneas y enviar una por una
            lines = text.split('\n')
            for line in lines:
                if line.strip():  # Solo enviar líneas no vacías
                    self.process.write((line + "\n").encode('utf-8'))
            
            # Enviar línea vacía al final para asegurar ejecución
            self.process.write("\n".encode('utf-8'))
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error en envío: {str(e)}")
    
    def get_terminal_text(self):
        """Retorna todo el texto del terminal"""
        return self.terminal_output.toPlainText()
    
    def is_running(self):
        """Verifica si el terminal está ejecutándose"""
        return self.process and self.process.state() == QProcess.ProcessState.Running

    # --- Compatibilidad con interfaz anterior ---
    def execute_code_from_editor(self, code: str):
        """Ejecuta código Python según modo seleccionado.

        Modos:
        - clean: ejecuta en subprocess y solo muestra stdout/stderr
        - interactive: envía el código al REPL embebido (prompts visibles)
        """
        try:
            # Asegurar ejecución en hilo GUI
            try:
                from PySide6.QtCore import QCoreApplication, QThread, QMetaObject, Qt as _Qt
                app = QCoreApplication.instance()
                if app and QThread.currentThread() is not app.thread():
                    # Re-dispatch completo en hilo GUI
                    code_copy = str(code)
                    QMetaObject.invokeMethod(self, lambda: self.execute_code_from_editor(code_copy), _Qt.QueuedConnection)
                    return True
            except Exception:
                pass
            if not code or not code.strip():
                return False

            def _safe_log(msg, color="#8888FF"):
                try:
                    self.terminal_output.setTextColor(QColor(color))
                    self.terminal_output.append(msg)
                    self.terminal_output.setTextColor(QColor('#FFFFFF'))
                except Exception:
                    pass

            # Disparo temprano de precaptura (independiente de auto-detect) si modo limpio
            # Resolver modo actual de forma robusta (userData o texto visible)
            current_mode = 'clean'
            if hasattr(self, 'exec_mode_combo'):
                try:
                    data = self.exec_mode_combo.currentData()
                    if data:
                        current_mode = data
                    else:
                        txt = self.exec_mode_combo.currentText().lower()
                        if 'inter' in txt:
                            current_mode = 'interactive'
                except Exception:
                    pass

            # Detección temprana de necesidad de precaptura (regex rápida)
            import re
            has_input_call = re.search(r'\binput\s*\(', code) is not None or 'getpass(' in code or 'stdin.readline' in code
            # Fallback temprano si GUI logging falló y estamos en modo limpio: ejecutar con placeholders para no bloquear
            if current_mode == 'clean' and has_input_call and not hasattr(self, 'terminal_output'):
                # Conteo rápido de inputs
                count_inputs = len(re.findall(r'\binput\s*\(', code)) or 1
                placeholders = ['0'] * count_inputs
                placeholder_wrapper = ['__ejecutate_inputs = iter(['] + [f"    {repr(v)}," for v in placeholders] + ['])','def input(prompt=None):','    try:','        val = next(__ejecutate_inputs)','    except StopIteration:','        val = ""','    if prompt: print(prompt, end="")','    return val','']
                final_code = "\n".join(placeholder_wrapper) + code
                import subprocess, sys
                proc = subprocess.run([sys.executable,'-u','-c',final_code], capture_output=True, text=True, timeout=3)
                print(proc.stdout, end='')
                print(proc.stderr, end='', file=sys.stderr)
                return True
            if current_mode == 'clean':
                prec = getattr(self, 'precapture_checkbox', None)
                if prec and prec.isChecked() and has_input_call:
                    if getattr(self, '_precapturing', False):
                        self.terminal_output.append("(info) Precaptura ya en curso...")
                    else:
                        def launch_precapture():
                            self._precapturing = True
                            _safe_log("🔍 Precaptura: se detectó input() en modo limpio. Mostrando diálogo.", "#87CEEB")
                            ok_local = self._pre_capture_and_run(code)
                            self._precapturing = False
                            return ok_local
                        # Invocar en hilo GUI seguro
                        try:
                            from PySide6.QtCore import QMetaObject, Qt as _Qt
                            QMetaObject.invokeMethod(self, lambda: launch_precapture(), _Qt.QueuedConnection)
                            return True
                        except Exception:
                            ok = launch_precapture()
                            if ok:
                                return True

            auto_detect = getattr(self, 'auto_detect_checkbox', None)
            needs_interactive = False
            if not auto_detect or auto_detect.isChecked():
                # Normalizar para análisis (minúsculas)
                norm_code = code.lower()
                import re
                input_pattern = re.compile(r'\binput\s*\(')
                interactive_tokens = [
                    bool(input_pattern.search(norm_code)),
                    'getpass(' in norm_code,
                    'stdin.readline' in norm_code,
                ]
                if 'while true' in norm_code and 'input(' in norm_code:
                    interactive_tokens.append(True)
                is_ast_interactive = False
                try:
                    if not any(interactive_tokens):
                        is_ast_interactive = self._is_interactive_code(code)
                except Exception:
                    pass
                needs_interactive = any(interactive_tokens) or is_ast_interactive

            mode = "clean"
            if hasattr(self, 'exec_mode_combo'):
                mode = self.exec_mode_combo.currentData()

            if needs_interactive:
                # Si precaptura activada, ejecutar simulando inputs en modo limpio
                if getattr(self, 'precapture_checkbox', None) and self.precapture_checkbox.isChecked():
                    return self._pre_capture_and_run(code)
                if mode != "interactive":
                    if hasattr(self, 'exec_mode_combo'):
                        for i in range(self.exec_mode_combo.count()):
                            if self.exec_mode_combo.itemData(i) == "interactive":
                                self.exec_mode_combo.setCurrentIndex(i)
                                break
                    self.terminal_output.setTextColor(QColor("#F1C40F"))
                    self.terminal_output.append("⚠️ Código interactivo detectado. Ejecutando en modo Interactivo.")
                    self.terminal_output.setTextColor(QColor("#FFFFFF"))
                    mode = "interactive"

            if mode == "interactive":
                return self._run_code_interactive(code)
            else:  # clean
                import subprocess, sys, threading, queue

                code_to_run = code.rstrip("\n") + "\n"

                # Cola para comunicar resultados sin bloquear UI
                result_q = queue.Queue()

                def worker():
                    try:
                        proc = subprocess.Popen(
                            [sys.executable, "-u", "-c", code_to_run],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        try:
                            stdout, stderr = proc.communicate(input="", timeout=0.4)
                            result_q.put((stdout, stderr, proc.returncode, False))
                        except subprocess.TimeoutExpired:
                            proc.kill()
                            stdout, stderr = proc.communicate()
                            result_q.put((stdout, stderr, proc.returncode, True))
                    except Exception as e:
                        result_q.put(("", f"Error ejecución: {e}", -1, False))

                threading.Thread(target=worker, daemon=True).start()

                # Programar sondeo no bloqueante
                def poll_result():
                    if not result_q.empty():
                        stdout, stderr, returncode, timed_out = result_q.get()
                        if timed_out or 'EOF when reading a line' in (stderr or ''):
                            auto_detect = getattr(self, 'auto_detect_checkbox', None)
                            if auto_detect and auto_detect.isChecked():
                                # Fallback automático
                                msg = "⏳ Código no terminó (posible input). Reejecutando en modo Interactivo..." if timed_out else "⚠️ Entrada requerida. Cambiando a interactivo..."
                                self.terminal_output.setTextColor(QColor("#F1C40F"))
                                self.terminal_output.append(msg)
                                self.terminal_output.setTextColor(QColor("#FFFFFF"))
                                if hasattr(self, 'exec_mode_combo'):
                                    for i in range(self.exec_mode_combo.count()):
                                        if self.exec_mode_combo.itemData(i) == "interactive":
                                            self.exec_mode_combo.setCurrentIndex(i)
                                            break
                                self.execute_code_from_editor(code)
                                return
                            else:
                                # Auto-detect desactivado: informar sin reejecutar
                                self.terminal_output.setTextColor(QColor("#F1C40F"))
                                warn = "⏳ Posible espera de input. Cambia a modo Interactivo o activa Auto-detect." if timed_out else "⚠️ Se detectó espera de entrada. Usa modo Interactivo."
                                self.terminal_output.append(warn)
                                self.terminal_output.setTextColor(QColor("#FFFFFF"))
                                # Mostrar lo capturado hasta ahora y salir
                                if stdout:
                                    self.terminal_output.setTextColor(QColor("#00FF00"))
                                    self.terminal_output.append(stdout.rstrip("\n"))
                                    self.terminal_output.setTextColor(QColor("#FFFFFF"))
                                if stderr:
                                    self.terminal_output.setTextColor(QColor("#FF5555"))
                                    self.terminal_output.append(stderr.rstrip("\n"))
                                    self.terminal_output.setTextColor(QColor("#FFFFFF"))
                                return
                        # Mostrar salida normal
                        if stdout:
                            self.terminal_output.setTextColor(QColor("#00FF00"))
                            self.terminal_output.append(stdout.rstrip("\n"))
                            self.terminal_output.setTextColor(QColor("#FFFFFF"))
                        if stderr:
                            self.terminal_output.setTextColor(QColor("#FF5555"))
                            self.terminal_output.append(stderr.rstrip("\n"))
                            self.terminal_output.setTextColor(QColor("#FFFFFF"))
                        if returncode != 0 and not stderr:
                            self.terminal_output.setTextColor(QColor("#FF5555"))
                            self.terminal_output.append(f"(exit code {returncode})")
                            self.terminal_output.setTextColor(QColor("#FFFFFF"))
                        # Auto-scroll
                        scrollbar = self.terminal_output.verticalScrollBar()
                        scrollbar.setValue(scrollbar.maximum())
                        return
                    # Repetir sondeo hasta recibir resultado
                    QTimer.singleShot(120, poll_result)

                poll_result()
                return True
        except Exception as e:
            self.terminal_output.setTextColor(QColor("#FF5555"))
            self.terminal_output.append(f"❌ Error ejecutando código: {e}")
            self.terminal_output.setTextColor(QColor("#FFFFFF"))
            return False

    def _run_code_interactive(self, code: str) -> bool:
        """Envía un bloque de código al REPL asegurando que el intérprete Python esté listo."""
        try:
            if self.shell_combo.currentData() != sys.executable:
                self.shell_combo.setCurrentIndex(0)
                self.change_shell()
                QTimer.singleShot(500, lambda: self._run_code_interactive(code))
                return True
            if not self.process or self.process.state() != QProcess.ProcessState.Running:
                self.start_terminal()
                QTimer.singleShot(600, lambda: self._run_code_interactive(code))
                return True

            # Mostrar aviso opcional solo primera línea si incluye input
            if 'input(' in code and '⚡ Interactivo listo' not in self.get_terminal_text():
                self.terminal_output.setTextColor(QColor("#87CEEB"))
                self.terminal_output.append("⚡ Interactivo listo: escribe respuestas y Enter para cada input().")
                self.terminal_output.setTextColor(QColor("#FFFFFF"))

            for line in code.split('\n'):
                self.process.write((line + "\n").encode('utf-8'))
            self.process.write("\n".encode('utf-8'))

            scrollbar = self.terminal_output.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            return True
        except Exception as e:
            self.terminal_output.setTextColor(QColor("#FF5555"))
            self.terminal_output.append(f"❌ Error modo interactivo: {e}")
            self.terminal_output.setTextColor(QColor("#FFFFFF"))
            return False

    # --- Pre-captura de inputs ---
    def _extract_input_prompts(self, code: str):
        """Extrae prompts de llamadas a input() en orden.
        Devuelve lista de tuplas (prompt_text_or_None, line_no)."""
        results = []
        try:
            import ast
            tree = ast.parse(code)
            class V(ast.NodeVisitor):
                def visit_Call(self, node):
                    try:
                        if isinstance(node.func, ast.Name) and node.func.id == 'input':
                            prompt = None
                            if node.args:
                                arg0 = node.args[0]
                                if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str):
                                    prompt = arg0.value
                            results.append((prompt, getattr(node, 'lineno', -1)))
                    except Exception:
                        pass
                    self.generic_visit(node)
            V().visit(tree)
        except Exception:
            pass
        return results

    def _pre_capture_and_run(self, code: str) -> bool:
        """Recoge valores para input() y ejecuta el código simulando entradas en modo limpio."""
        prompts = self._extract_input_prompts(code)
        if not prompts:
            # Nada que precapturar; fallback a modo interactivo para no entrar en loop
            return self._run_code_interactive(code)
        values = []
        # Atajo para pruebas automatizadas (sin GUI)
        test_env = os.getenv("EJECUTATE_TEST_INPUTS")
        if test_env:
            try:
                import json as _json
                parsed = _json.loads(test_env)
                if isinstance(parsed, list):
                    values = [str(v) for v in parsed]
            except Exception:
                pass
        if not values:
            # Construir diálogo no bloqueante
            try:
                dialog = QDialog(self)
                dialog.setWindowTitle("Precapturar inputs")
                dialog.setWindowModality(Qt.ApplicationModal)
                layout = QVBoxLayout(dialog)
                form = QFormLayout()
                edits = []
                for idx, (prompt, lineno) in enumerate(prompts, 1):
                    label = prompt if prompt else f"input #{idx}"; label = (label[:40] + '...') if len(label) > 43 else label
                    edit = QLineEdit()
                    form.addRow(QLabel(label), edit)
                    edits.append(edit)
                layout.addLayout(form)
                buttons_layout = QHBoxLayout()
                ok_btn = QPushButton("Ejecutar")
                cancel_btn = QPushButton("Cancelar")
                buttons_layout.addStretch()
                buttons_layout.addWidget(cancel_btn)
                buttons_layout.addWidget(ok_btn)
                layout.addLayout(buttons_layout)

                self._precapture_dialog = dialog  # mantener referencia
                self.terminal_output.setTextColor(QColor("#87CEEB"))
                self.terminal_output.append(f"📝 Precaptura: {len(prompts)} input(s) detectado(s). Introduce valores y pulsa Ejecutar.")
                self.terminal_output.setTextColor(QColor("#FFFFFF"))

                def on_accept():
                    vals = [e.text() for e in edits]
                    dialog.close()
                    # Re-entrar a ejecución final con valores
                    self._finish_precapture_execution(code, vals)

                def on_reject():
                    dialog.close()
                    self.terminal_output.append("🚫 Ejecución cancelada.")

                ok_btn.clicked.connect(on_accept)
                cancel_btn.clicked.connect(on_reject)
                dialog.show()  # no bloquea

                # Fallback de seguridad: si en 2s no se capturó (usuario no interactúa), cambiar a interactivo
                def fallback_if_not_closed():
                    if getattr(self, '_precapture_dialog', None) is dialog and dialog.isVisible():
                        self.terminal_output.setTextColor(QColor("#F1C40F"))
                        self.terminal_output.append("⏳ Sin respuesta en precaptura. Cambiando a modo Interactivo.")
                        self.terminal_output.setTextColor(QColor("#FFFFFF"))
                        if hasattr(self, 'exec_mode_combo'):
                            for i in range(self.exec_mode_combo.count()):
                                if 'inter' in self.exec_mode_combo.itemText(i).lower():
                                    self.exec_mode_combo.setCurrentIndex(i)
                                    break
                        dialog.close()
                        self._run_code_interactive(code)
                QTimer.singleShot(2000, fallback_if_not_closed)
                return True
            except Exception as e:
                self.terminal_output.append(f"❌ Error diálogo precaptura: {e}. Fallback interactivo.")
                return self._run_code_interactive(code)

        # Si llegamos aquí, tenemos values por variable de entorno y ejecutamos directo
        return self._finish_precapture_execution(code, values)

    def _finish_precapture_execution(self, code: str, values):
        """Compone wrapper de inputs y lanza ejecución asíncrona limpia."""
        import json as _json
        wrapper = ['__ejecutate_inputs = iter([']
        for v in values:
            wrapper.append(f"    {_json.dumps(v)},")
        wrapper.append('])')
        wrapper.append('def input(prompt=None):')
        wrapper.append('    try:')
        wrapper.append('        val = next(__ejecutate_inputs)')
        wrapper.append('    except StopIteration:')
        wrapper.append('        val = ""')
        wrapper.append('    if prompt:')
        wrapper.append('        print(prompt, end="")')
        wrapper.append('    return val')
        wrapper.append('')
        final_code = "\n".join(wrapper) + "\n" + code

        # Ejecutar en modo limpio forzado (subprocess corto)
        try:
            import subprocess, sys, threading, queue

            q = queue.Queue()
            code_to_run = final_code

            def worker():
                try:
                    proc = subprocess.Popen([sys.executable, '-u', '-c', code_to_run], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    stdout, stderr = proc.communicate()
                    q.put((stdout, stderr, proc.returncode))
                except Exception as e:
                    q.put(("", f"Error: {e}", -1))

            threading.Thread(target=worker, daemon=True).start()

            self.terminal_output.setTextColor(QColor("#87CEEB"))
            self.terminal_output.append("⏳ Ejecutando con inputs precapturados (no bloquea GUI)...")
            self.terminal_output.setTextColor(QColor("#FFFFFF"))

            def poll():
                if not q.empty():
                    stdout, stderr, rc = q.get()
                    if stdout:
                        self.terminal_output.setTextColor(QColor("#00FF00"))
                        self.terminal_output.append(stdout.rstrip('\n'))
                        self.terminal_output.setTextColor(QColor("#FFFFFF"))
                    if stderr:
                        self.terminal_output.setTextColor(QColor("#FF5555"))
                        self.terminal_output.append(stderr.rstrip('\n'))
                        self.terminal_output.setTextColor(QColor("#FFFFFF"))
                    if rc != 0 and not stderr:
                        self.terminal_output.setTextColor(QColor("#FF5555"))
                        self.terminal_output.append(f"(exit code {rc})")
                        self.terminal_output.setTextColor(QColor("#FFFFFF"))
                    return
                QTimer.singleShot(120, poll)

            QTimer.singleShot(120, poll)
            return True
        except Exception as e:
            self.terminal_output.append(f"❌ Error ejecutando con precaptura: {e}")
            return False
    def _is_interactive_code(self, code: str) -> bool:
        """Heurística para detectar si el código requiere entrada del usuario.

        Implementación:
        1. Parseo AST buscando llamadas a input / getpass / sys.stdin.
        2. Búsqueda rápida de patrones en texto (fallback si AST falla).
        """
        try:
            import ast, re
            tree = ast.parse(code)
            interactive_funcs = {"input", "getpass"}
            class InputVisitor(ast.NodeVisitor):
                def __init__(self):
                    self.found = False
                def _node_has_input(self, node):
                    # Busca llamadas a input dentro de nodo
                    for child in ast.walk(node):
                        if isinstance(child, ast.Call):
                            if isinstance(child.func, ast.Name) and child.func.id in interactive_funcs:
                                return True
                            if isinstance(child.func, ast.Attribute) and getattr(child.func.value, 'id', '') == 'sys' and child.func.attr.startswith('stdin'):
                                return True
                    return False
                def visit_Call(self, node):
                    try:
                        if isinstance(node.func, ast.Name) and node.func.id in interactive_funcs:
                            self.found = True
                        elif isinstance(node.func, ast.Attribute):
                            # sys.stdin.readline, etc.
                            if getattr(node.func.value, 'id', '') == 'sys' and node.func.attr in ('stdin', 'stdin.readline'):
                                self.found = True
                    except Exception:
                        pass
                    self.generic_visit(node)
                def visit_While(self, node):
                    # Detectar while True con input dentro
                    if isinstance(node.test, ast.Constant) and node.test.value is True:
                        if self._node_has_input(node):
                            self.found = True
                    self.generic_visit(node)
                def visit_For(self, node):
                    if self._node_has_input(node):
                        self.found = True
                    self.generic_visit(node)
            visitor = InputVisitor()
            visitor.visit(tree)
            if visitor.found:
                return True
        except Exception:
            # Ignorar errores de parseo y usar regex
            pass
        # Fallback textual (evitar falsos positivos básicos)
        pattern = r'(^|[^\w])input\s*\('  # input(
        if re.search(pattern, code):
            return True
        if 'getpass(' in code:
            return True
        if 'stdin.readline' in code:
            return True
        return False

    def _persist_auto_detect(self, state: int):
        """Guarda el estado del checkbox Auto-detect en QSettings."""
        try:
            settings = QSettings("Ejecutate", "EditorPython")
            settings.setValue("terminal/auto_detect", bool(state))
        except Exception:
            pass

    def _persist_precapture(self, state: int):
        """Guarda el estado del checkbox de precaptura en QSettings."""
        try:
            settings = QSettings("Ejecutate", "EditorPython")
            settings.setValue("terminal/precapture", bool(state))
        except Exception:
            pass
