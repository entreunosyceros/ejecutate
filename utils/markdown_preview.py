"""Vista previa de Markdown y utilidades de tipo de archivo."""

from __future__ import annotations

import html
import os
import re

from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QSplitter,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

MARKDOWN_EXTENSIONS = {".md", ".markdown"}
NON_EXECUTABLE_EXTENSIONS = {".txt", ".md", ".markdown"}


def is_markdown_path(path: str | None) -> bool:
    if not path:
        return False
    return os.path.splitext(path)[1].lower() in MARKDOWN_EXTENSIONS


def is_executable_path(path: str | None) -> bool:
    """Archivos .txt y .md no deben ejecutarse como código Python."""
    if not path:
        return True
    return os.path.splitext(path)[1].lower() not in NON_EXECUTABLE_EXTENSIONS


def _fallback_markdown_to_html(text: str) -> str:
    """Conversión mínima si la librería markdown no está instalada."""
    escaped = html.escape(text)
    escaped = re.sub(r"^### (.+)$", r"<h3>\1</h3>", escaped, flags=re.MULTILINE)
    escaped = re.sub(r"^## (.+)$", r"<h2>\1</h2>", escaped, flags=re.MULTILINE)
    escaped = re.sub(r"^# (.+)$", r"<h1>\1</h1>", escaped, flags=re.MULTILINE)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        escaped,
    )
    paragraphs = "<p>" + escaped.replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"
    return paragraphs


def render_markdown_html(text: str) -> str:
    body = ""
    try:
        import markdown

        body = markdown.markdown(
            text or "",
            extensions=["fenced_code", "tables", "nl2br", "sane_lists"],
        )
    except Exception:
        body = _fallback_markdown_to_html(text or "")

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 14px;
    line-height: 1.55;
    padding: 14px 18px;
    margin: 0;
    background: #1e1e1e;
    color: #d4d4d4;
}}
h1, h2, h3, h4 {{ color: #569cd6; margin-top: 1.2em; }}
a {{ color: #3794ff; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
code {{
    font-family: Consolas, monospace;
    background: #2d2d2d;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 13px;
}}
pre {{
    background: #252526;
    border: 1px solid #3c3c3c;
    border-radius: 6px;
    padding: 12px;
    overflow-x: auto;
}}
pre code {{ background: transparent; padding: 0; }}
blockquote {{
    border-left: 3px solid #555;
    margin: 0.8em 0;
    padding: 0.2em 0 0.2em 14px;
    color: #b0b0b0;
}}
table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
th, td {{ border: 1px solid #444; padding: 6px 10px; }}
th {{ background: #2a2a2a; }}
hr {{ border: none; border-top: 1px solid #444; margin: 1.5em 0; }}
ul, ol {{ padding-left: 1.4em; }}
</style></head><body>{body}</body></html>"""


class MarkdownEditorTab(QWidget):
    """Pestaña Markdown: editor + previsualización opcional."""

    visibilityChanged = Signal(bool)

    def __init__(self, editor, parent=None, preview_visible: bool = False):
        super().__init__(parent)
        self.editor = editor
        self._preview_visible = preview_visible

        self.preview_toggle_btn = QPushButton("👁️ Vista previa")
        self.preview_toggle_btn.setCheckable(True)
        self.preview_toggle_btn.setChecked(preview_visible)
        self.preview_toggle_btn.setToolTip("Mostrar u ocultar vista previa (Ctrl+Shift+V)")
        self.preview_toggle_btn.clicked.connect(self._on_toggle_clicked)
        self.preview_toggle_btn.setStyleSheet("""
            QPushButton {
                background: #34495E;
                color: #ECF0F1;
                border: none;
                padding: 4px 10px;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover { background: #3D566E; }
            QPushButton:checked {
                background: #3498DB;
                color: white;
                font-weight: bold;
            }
        """)

        toolbar = QHBoxLayout()
        toolbar.setContentsMargins(4, 4, 4, 0)
        toolbar.addWidget(self.preview_toggle_btn)
        toolbar.addStretch()

        self.preview = QTextBrowser()
        self.preview.setOpenExternalLinks(True)
        self.preview.setStyleSheet(
            "QTextBrowser { background: #1e1e1e; border: none; border-left: 1px solid #3c3c3c; }"
        )
        self.preview.setVisible(preview_visible)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(editor)
        self.splitter.addWidget(self.preview)
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 1)
        if preview_visible:
            self.splitter.setSizes([500, 500])
        else:
            self.splitter.setSizes([1000, 0])

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addLayout(toolbar)
        layout.addWidget(self.splitter, 1)

        self._preview_timer = QTimer(self)
        self._preview_timer.setSingleShot(True)
        self._preview_timer.setInterval(250)
        self._preview_timer.timeout.connect(self.update_preview)

        QShortcut(QKeySequence("Ctrl+Shift+V"), self, self.toggle_preview)

    def _on_toggle_clicked(self, checked: bool):
        self.set_preview_visible(checked)

    def is_preview_visible(self) -> bool:
        return self._preview_visible

    def toggle_preview(self):
        self.set_preview_visible(not self._preview_visible)

    def set_preview_visible(self, visible: bool):
        if self._preview_visible == visible:
            return
        self._preview_visible = visible
        self.preview_toggle_btn.blockSignals(True)
        self.preview_toggle_btn.setChecked(visible)
        self.preview_toggle_btn.blockSignals(False)
        self.preview.setVisible(visible)
        if visible:
            self.update_preview()
            total = max(self.splitter.width(), 800)
            self.splitter.setSizes([total // 2, total // 2])
        else:
            self.splitter.setSizes([1000, 0])
        self.visibilityChanged.emit(visible)

    def schedule_preview_update(self):
        if self._preview_visible:
            self._preview_timer.start()

    def update_preview(self):
        self.preview.setHtml(render_markdown_html(self.editor.toPlainText()))


def get_editor_widget(tab_widget) -> "PythonCodeEditor | None":
    """Obtiene el QPlainTextEdit editor desde una pestaña (con o sin preview)."""
    if tab_widget is None:
        return None
    if isinstance(tab_widget, MarkdownEditorTab):
        return tab_widget.editor
    return tab_widget


def get_markdown_tab(tab_widget) -> MarkdownEditorTab | None:
    if isinstance(tab_widget, MarkdownEditorTab):
        return tab_widget
    return None
