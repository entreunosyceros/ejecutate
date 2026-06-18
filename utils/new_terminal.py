#!/usr/bin/env python3
"""
Terminal integrado real usando QProcess
Este archivo contiene la nueva implementación del terminal
"""

import time
import os
import shutil
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
        self._shell_switch_pending = False
        self._pending_shell_banner = None
        self.setup_ui()
        self.start_terminal()

    def _available_interpreters(self):
        """Intérpretes instalados en el sistema (solo rutas ejecutables)."""
        venv_path = os.environ.get("VIRTUAL_ENV")
        py_label = "🐍 Python (venv)" if venv_path else "🐍 Python"
        py_exec = sys.executable or shutil.which("python3") or shutil.which("python")

        specs = [
            ("python", py_label, py_exec),
            ("bash", "🐧 Bash", shutil.which("bash")),
            ("zsh", "🐚 Zsh", shutil.which("zsh")),
            ("fish", "🐟 Fish", shutil.which("fish")),
            ("sh", "📱 Sh", shutil.which("sh")),
        ]
        available = []
        for kind, label, path in specs:
            if not path:
                continue
            if os.path.isfile(path) and os.access(path, os.X_OK):
                resolved = os.path.realpath(path)
                if kind == "sh":
                    base = os.path.basename(resolved).lower()
                    if base == "dash":
                        label = "📱 Sh (dash)"
                available.append((label, resolved, kind))
        if not available and py_exec:
            available.append((py_label, py_exec, "python"))
        return available

    def _populate_shell_combo(self):
        """Rellena el selector solo con intérpretes disponibles."""
        self.shell_combo.blockSignals(True)
        previous_kind = self._shell_kind()
        self.shell_combo.clear()
        for label, path, kind in self._available_interpreters():
            self.shell_combo.addItem(label, {"path": path, "kind": kind})
        if previous_kind:
            for i in range(self.shell_combo.count()):
                if self._shell_kind(i) == previous_kind:
                    self.shell_combo.setCurrentIndex(i)
                    break
        self.shell_combo.blockSignals(False)

    def _shell_meta(self, index=None):
        if index is None:
            index = self.shell_combo.currentIndex()
        if index < 0:
            return None
        data = self.shell_combo.itemData(index)
        if isinstance(data, dict):
            return data
        if isinstance(data, str):
            kind = "python" if "python" in os.path.basename(data).lower() else "shell"
            return {"path": data, "kind": kind}
        return None

    def _shell_path(self, index=None):
        meta = self._shell_meta(index)
        return meta.get("path") if meta else None

    def _shell_kind(self, index=None):
        meta = self._shell_meta(index)
        return meta.get("kind") if meta else None

    def _python_combo_index(self):
        for i in range(self.shell_combo.count()):
            if self._shell_kind(i) == "python":
                return i
        return 0

    def _bash_combo_index(self) -> int | None:
        for i in range(self.shell_combo.count()):
            if self._shell_kind(i) == "bash":
                return i
        return None

    def _is_python_repl_shell(self) -> bool:
        return self._shell_kind() == "python"

    def _set_shell_combo_index(self, index: int):
        self.shell_combo.blockSignals(True)
        self.shell_combo.setCurrentIndex(index)
        self.shell_combo.blockSignals(False)
        self.change_shell()

    def setup_ui(self):
        """Configura la interfaz del terminal (versión corregida)"""
        layout = QVBoxLayout()
        toolbar = QHBoxLayout()

        # Intérprete
        self.shell_combo = QComboBox()
        self._populate_shell_combo()
        self.shell_combo.setToolTip(
            "Solo aparecen intérpretes instalados en este equipo "
            "(detectados con PATH y rutas del sistema)."
        )
        self.shell_combo.currentIndexChanged.connect(self._on_shell_index_changed)

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
        self.exec_mode_combo.setToolTip(
            "Solo afecta a comandos escritos a mano en la caja del terminal. "
            "El botón «Ejecutar Código» del editor siempre lanza el programa completo."
        )

        # Auto-detect persistente
        self.auto_detect_checkbox = QCheckBox("🧠 Auto-detect")
        try:
            settings = QSettings("Ejecutate", "EditorPython")
            self.auto_detect_checkbox.setChecked(settings.value("terminal/auto_detect", True, type=bool))
        except Exception:
            self.auto_detect_checkbox.setChecked(True)
        self.auto_detect_checkbox.setToolTip(
            "Solo para la caja de comandos del terminal. "
            "No cambia cómo funciona «Ejecutar Código» en el editor."
        )
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

    def _stop_process(self, wait_ms: int = 800):
        """Detiene el QProcess del shell si sigue en ejecución."""
        proc = self.process
        if not proc:
            return
        try:
            if proc.state() == QProcess.ProcessState.Running:
                proc.kill()
                proc.waitForFinished(wait_ms)
        except Exception:
            pass

    def _on_shell_index_changed(self, _index: int):
        """Cambio de intérprete desde el combo (evita reentrada)."""
        if self._shell_switch_pending:
            return
        self.change_shell()

    def _shell_start_args(self, path: str, kind: str) -> list:
        """Argumentos de arranque. dash/POSIX sh no admiten -i (solo bash/zsh)."""
        if kind == "python":
            return ["-i", "-u"]
        if kind == "fish":
            return []
        real_base = os.path.basename(os.path.realpath(path)).lower()
        if real_base == "dash" or kind == "sh":
            return []
        if real_base in ("bash", "zsh") or kind in ("bash", "zsh"):
            return ["-i"]
        return []

    def _launch_shell(self) -> bool:
        """Arranca el intérprete seleccionado (entorno configurado antes de start)."""
        if not self.process:
            return False

        path = self._shell_path()
        kind = self._shell_kind()
        shell_name = self.shell_combo.currentText()

        if not path or not os.path.isfile(path) or not os.access(path, os.X_OK):
            self.terminal_output.append(f"❌ Intérprete no disponible: {path or shell_name}")
            self.status_label.setText("🔴 Intérprete no disponible")
            self.status_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
            return False

        env = QProcessEnvironment.systemEnvironment()
        env.insert("PYTHONUNBUFFERED", "1")
        env.insert("PYTHONIOENCODING", "utf-8")
        env.insert("TERM", "xterm-256color")
        env.insert("COLUMNS", "80")
        env.insert("LINES", "24")
        if kind == "bash":
            env.insert("PS1", r"\u@\h:\w$ ")
        elif kind == "zsh":
            env.insert("PS1", "%n@%m:%~ %# ")

        self.process.setProcessEnvironment(env)
        self._pending_shell_banner = shell_name
        self.process.start(path, self._shell_start_args(path, kind))
        return True

    def _finish_shell_change(self):
        """Continúa el cambio de intérprete tras cerrar el proceso anterior (sin bloquear la GUI)."""
        if not self._shell_switch_pending:
            return
        if self.process and self.process.state() == QProcess.ProcessState.Running:
            QTimer.singleShot(100, self._finish_shell_change)
            return
        try:
            self._launch_shell()
        except Exception as e:
            self.terminal_output.append(f"❌ Error al cambiar shell: {str(e)}")
        finally:
            self._shell_switch_pending = False

    def change_shell(self):
        """Cambia el shell del terminal de forma segura."""
        if self._shell_switch_pending:
            return
        try:
            if not self.process:
                self.start_terminal()
                return

            self._shell_switch_pending = True
            if self.process.state() == QProcess.ProcessState.Running:
                self.process.kill()
            QTimer.singleShot(120, self._finish_shell_change)
        except Exception as e:
            self._shell_switch_pending = False
            self.terminal_output.append(f"❌ Error al cambiar shell: {str(e)}")

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
            self.process.errorOccurred.connect(self.handle_process_error)
            
            self.change_shell()
            
        except Exception as e:
            self.terminal_output.append(f"❌ Error al inicializar terminal: {str(e)}")

    def handle_process_error(self, error):
        """Errores de arranque del intérprete (p. ej. ejecutable inexistente)."""
        self._pending_shell_banner = None
        if error == QProcess.ProcessError.FailedToStart:
            shell_name = self.shell_combo.currentText()
            self.terminal_output.append(
                f"\n❌ No se pudo iniciar {shell_name}: {self.process.errorString()}"
            )
            self.status_label.setText("🔴 Intérprete no disponible")
            self.status_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
    
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

            banner = getattr(self, "_pending_shell_banner", None)
            if banner:
                self._pending_shell_banner = None
                self.terminal_output.clear()
                self.terminal_output.append(f"🚀 Iniciando {banner}...")
                self.terminal_output.append("=" * 50)

            shell_kind = self._shell_kind()
            if shell_kind == "python":
                init_commands = [
                    "import sys",
                    "sys.ps1 = '🐍 >>> '",
                    "sys.ps2 = '🐍 ... '",
                    "print('🐍 Python interactivo listo!')"
                ]
                for cmd in init_commands:
                    self.process.write((cmd + "\n").encode('utf-8'))
            elif shell_kind == "fish":
                self.process.write("echo '🐚 Terminal listo!'\n".encode('utf-8'))
            else:
                self.process.write("echo 'Terminal listo!'\n".encode('utf-8'))
        except Exception as e:
            self.terminal_output.append(f"❌ Error inicializando shell: {e}")
    
    def handle_finished(self, exit_code):
        """Maneja cuando el proceso termina"""
        if self._shell_switch_pending:
            return
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

            self._populate_shell_combo()
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
            if not self._is_python_repl_shell():
                py_idx = self._python_combo_index()
                self._set_shell_combo_index(py_idx)
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

    def _looks_like_standalone_script(self, code: str) -> bool:
        """Detecta scripts que deben ejecutarse como archivo, no en el REPL línea a línea."""
        import re
        if not code or not code.strip():
            return False
        if "__file__" in code:
            return True
        if re.search(r"""if\s+__name__\s*==\s*(['"])__main__\1""", code):
            return True
        if code.lstrip().startswith("#!"):
            return True
        if len(re.findall(r"^def \w+\(", code, re.MULTILINE)) >= 2:
            return True
        if len(code.splitlines()) > 35:
            return True
        return False

    def _materialize_script_file(
        self,
        code: str,
        file_path: str | None,
        cwd: str | None,
        *,
        as_program: bool = False,
    ) -> tuple[str | None, str | None]:
        """Resuelve la ruta del script a ejecutar (guardado o temporal)."""
        run_cwd = cwd
        if file_path:
            ext = os.path.splitext(file_path)[1].lower()
            if ext in (".py", ".pyw", ".pyi") and os.path.isfile(file_path):
                run_file = os.path.abspath(file_path)
                if not run_cwd:
                    run_cwd = os.path.dirname(run_file)
                return run_file, run_cwd
        if as_program or self._looks_like_standalone_script(code):
            directory = run_cwd if run_cwd and os.path.isdir(run_cwd) else os.getcwd()
            import tempfile
            fd, path = tempfile.mkstemp(suffix=".py", prefix="_ejecutalo_", dir=directory)
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    handle.write(code)
            except Exception:
                try:
                    os.unlink(path)
                except OSError:
                    pass
                raise
            if not run_cwd:
                run_cwd = directory
            return path, run_cwd
        return None, run_cwd

    def _run_program_in_embedded_shell(
        self,
        run_file: str,
        run_cwd: str | None,
        *,
        python_exe: str | None = None,
    ) -> bool:
        """Lanza un .py en el shell integrado para que stdin siga conectado (TUI, input, Rich)."""
        import shlex

        run_file = os.path.abspath(run_file)
        cwd = run_cwd or os.path.dirname(run_file) or os.getcwd()
        py = python_exe or sys.executable
        ctx = {"run_file": run_file, "cwd": cwd, "py": py}

        def launch():
            if not self.process or self.process.state() != QProcess.ProcessState.Running:
                self.start_terminal()
                QTimer.singleShot(900, launch)
                return

            self.terminal_output.setTextColor(QColor("#87CEEB"))
            self.terminal_output.append(f"\n▶ Ejecutando programa: {ctx['run_file']}")
            self.terminal_output.setTextColor(QColor("#FFFFFF"))
            self.terminal_output.append(
                "   Si el programa pide datos, escríbelos en la caja inferior y pulsa Enter.\n"
            )

            command = (
                f"cd {shlex.quote(ctx['cwd'])} && "
                f"{shlex.quote(ctx['py'])} -u {shlex.quote(ctx['run_file'])}\n"
            )
            self.process.write(command.encode("utf-8"))
            self.command_input.setFocus()
            self.status_label.setText("⚡ Programa en ejecución — usa la caja inferior")
            self.status_label.setStyleSheet("color: #F39C12; font-weight: bold;")

            scrollbar = self.terminal_output.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())

        def prepare():
            bash_idx = self._bash_combo_index()
            if self._is_python_repl_shell() and bash_idx is not None:
                if self.shell_combo.currentIndex() != bash_idx:
                    self._set_shell_combo_index(bash_idx)
                    QTimer.singleShot(900, launch)
                    return
            if not self.process or self.process.state() != QProcess.ProcessState.Running:
                self.start_terminal()
                QTimer.singleShot(900, launch)
                return
            launch()

        prepare()
        return True

    def _run_code_subprocess(
        self,
        code: str,
        run_file: str | None,
        run_cwd: str | None,
        *,
        file_path: str | None = None,
    ) -> bool:
        """Ejecuta código en subprocess sin bloquear la interfaz."""
        import subprocess
        import sys
        import threading
        import queue

        def _safe_log(msg, color="#8888FF"):
            try:
                self.terminal_output.setTextColor(QColor(color))
                self.terminal_output.append(msg)
                self.terminal_output.setTextColor(QColor("#FFFFFF"))
            except Exception:
                pass

        code_to_run = code.rstrip("\n") + "\n"
        result_q = queue.Queue()

        def worker():
            try:
                popen_kwargs = {
                    "stdin": subprocess.PIPE,
                    "stdout": subprocess.PIPE,
                    "stderr": subprocess.PIPE,
                    "text": True,
                }
                if run_cwd and os.path.isdir(run_cwd):
                    popen_kwargs["cwd"] = run_cwd
                if run_file:
                    proc = subprocess.Popen(
                        [sys.executable, "-u", run_file],
                        **popen_kwargs,
                    )
                else:
                    proc = subprocess.Popen(
                        [sys.executable, "-u", "-c", code_to_run],
                        **popen_kwargs,
                    )
                stdout, stderr = proc.communicate(input="")
                result_q.put((stdout, stderr, proc.returncode, False))
            except Exception as e:
                result_q.put(("", f"Error ejecución: {e}", -1, False))

        threading.Thread(target=worker, daemon=True).start()

        if run_file:
            _safe_log(f"▶ Ejecutando script: {run_file}", "#87CEEB")
        elif run_cwd:
            _safe_log(f"▶ Directorio de trabajo: {run_cwd}", "#666666")

        def poll_result():
            if not result_q.empty():
                stdout, stderr, returncode, _timed_out = result_q.get()
                if "EOF when reading a line" in (stderr or "") or "EOFError" in (stderr or ""):
                    self.terminal_output.setTextColor(QColor("#F1C40F"))
                    self.terminal_output.append(
                        "⚠️ El programa necesita entrada interactiva. "
                        "Vuelve a ejecutar: ahora se lanzará en el terminal integrado "
                        "y podrás escribir en la caja inferior."
                    )
                    self.terminal_output.setTextColor(QColor("#FFFFFF"))

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
                scrollbar = self.terminal_output.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
                return
            QTimer.singleShot(120, poll_result)

        poll_result()
        return True

    # --- Compatibilidad con interfaz anterior ---
    def execute_code_from_editor(self, code: str, file_path: str | None = None, cwd: str | None = None):
        """Ejecuta todo el contenido del editor como un programa Python.

        Siempre lanza el programa completo en el shell integrado (stdin conectado).
        Solo la precaptura de input() usa subprocess aislado.
        """
        try:
            # Asegurar ejecución en hilo GUI
            try:
                from PySide6.QtCore import QCoreApplication, QThread
                app = QCoreApplication.instance()
                if app and QThread.currentThread() is not app.thread():
                    code_copy = str(code)
                    fp_copy = file_path
                    cwd_copy = cwd
                    QTimer.singleShot(
                        0,
                        lambda c=code_copy, fp=fp_copy, cw=cwd_copy: self.execute_code_from_editor(
                            c, file_path=fp, cwd=cw
                        ),
                    )
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

            import re
            has_input_call = (
                re.search(r'\binput\s*\(', code) is not None
                or 'getpass(' in code
                or 'stdin.readline' in code
            )
            prec = getattr(self, 'precapture_checkbox', None)
            if prec and prec.isChecked() and has_input_call:
                if getattr(self, '_precapturing', False):
                    self.terminal_output.append("(info) Precaptura ya en curso...")
                else:
                    def launch_precapture(c):
                        self._precapturing = True
                        _safe_log(
                            "🔍 Precaptura: se detectó input(). Mostrando diálogo.",
                            "#87CEEB",
                        )
                        ok_local = self._pre_capture_and_run(c)
                        self._precapturing = False
                        return ok_local

                    try:
                        QTimer.singleShot(0, lambda c=code: launch_precapture(c))
                        return True
                    except Exception:
                        if launch_precapture(code):
                            return True

            run_file, run_cwd = self._materialize_script_file(
                code, file_path, cwd, as_program=True
            )
            if not run_file:
                return False
            return self._run_program_in_embedded_shell(run_file, run_cwd)
        except Exception as e:
            self.terminal_output.setTextColor(QColor("#FF5555"))
            self.terminal_output.append(f"❌ Error ejecutando código: {e}")
            self.terminal_output.setTextColor(QColor("#FFFFFF"))
            return False

    def _run_code_interactive(
        self,
        code: str,
        file_path: str | None = None,
        cwd: str | None = None,
    ) -> bool:
        """Envía fragmentos cortos al REPL. Los scripts completos van por subprocess."""
        run_file, run_cwd = self._materialize_script_file(code, file_path, cwd)
        if run_file:
            return self._run_program_in_embedded_shell(run_file, run_cwd)
        try:
            if not self._is_python_repl_shell():
                self._set_shell_combo_index(self._python_combo_index())
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
            run_file, run_cwd = self._materialize_script_file(
                code, None, None, as_program=True
            )
            if run_file:
                return self._run_program_in_embedded_shell(run_file, run_cwd)
            return False
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
                        self.execute_code_from_editor(code)
                QTimer.singleShot(2000, fallback_if_not_closed)
                return True
            except Exception as e:
                self.terminal_output.append(f"❌ Error diálogo precaptura: {e}.")
                return self.execute_code_from_editor(code)

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
