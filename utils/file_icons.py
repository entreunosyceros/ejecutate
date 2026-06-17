"""Iconos por tipo de archivo para el explorador lateral."""

from __future__ import annotations

import os
from functools import lru_cache

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QFileIconProvider

_icon_provider = QFileIconProvider()

# extensión -> (color fondo, etiqueta, color texto opcional)
_EXT_STYLES: dict[str, tuple[str, str, str]] = {
    ".py": ("#3572A5", "PY", "#FFFFFF"),
    ".pyw": ("#3572A5", "PY", "#FFFFFF"),
    ".pyi": ("#3572A5", "PY", "#FFFFFF"),
    ".pyc": ("#5C6370", "PC", "#FFFFFF"),
    ".ipynb": ("#F37626", "IP", "#FFFFFF"),
    ".js": ("#F1E05A", "JS", "#1F2328"),
    ".mjs": ("#F1E05A", "JS", "#1F2328"),
    ".cjs": ("#F1E05A", "JS", "#1F2328"),
    ".jsx": ("#53C1DE", "JX", "#1F2328"),
    ".ts": ("#3178C6", "TS", "#FFFFFF"),
    ".tsx": ("#3178C6", "TX", "#FFFFFF"),
    ".html": ("#E34C26", "HT", "#FFFFFF"),
    ".htm": ("#E34C26", "HT", "#FFFFFF"),
    ".css": ("#563D7C", "CS", "#FFFFFF"),
    ".scss": ("#C6538C", "SC", "#FFFFFF"),
    ".sass": ("#C6538C", "SA", "#FFFFFF"),
    ".less": ("#1D365D", "LE", "#FFFFFF"),
    ".json": ("#CBCB41", "JN", "#1F2328"),
    ".jsonc": ("#CBCB41", "JC", "#1F2328"),
    ".yaml": ("#CB171E", "YM", "#FFFFFF"),
    ".yml": ("#CB171E", "YM", "#FFFFFF"),
    ".toml": ("#9C422D", "TM", "#FFFFFF"),
    ".xml": ("#E37933", "XM", "#FFFFFF"),
    ".md": ("#083FA1", "MD", "#FFFFFF"),
    ".markdown": ("#083FA1", "MD", "#FFFFFF"),
    ".rst": ("#141414", "RS", "#FFFFFF"),
    ".txt": ("#6A737D", "TX", "#FFFFFF"),
    ".log": ("#6A737D", "LG", "#FFFFFF"),
    ".ini": ("#6A737D", "IN", "#FFFFFF"),
    ".cfg": ("#6A737D", "CF", "#FFFFFF"),
    ".conf": ("#6A737D", "CN", "#FFFFFF"),
    ".env": ("#ECD53F", "EN", "#1F2328"),
    ".sh": ("#4EAA25", "SH", "#FFFFFF"),
    ".bash": ("#4EAA25", "SH", "#FFFFFF"),
    ".zsh": ("#4EAA25", "ZS", "#FFFFFF"),
    ".fish": ("#4EAA25", "FS", "#FFFFFF"),
    ".ps1": ("#012456", "P1", "#FFFFFF"),
    ".bat": ("#4D5A5E", "BT", "#FFFFFF"),
    ".cmd": ("#4D5A5E", "CM", "#FFFFFF"),
    ".sql": ("#E38C00", "SQ", "#FFFFFF"),
    ".csv": ("#89E051", "CV", "#1F2328"),
    ".tsv": ("#89E051", "TS", "#1F2328"),
    ".java": ("#B07219", "JV", "#FFFFFF"),
    ".kt": ("#A97BFF", "KT", "#1F2328"),
    ".c": ("#555555", "C", "#FFFFFF"),
    ".h": ("#555555", "H", "#FFFFFF"),
    ".cpp": ("#F34B7D", "C+", "#FFFFFF"),
    ".hpp": ("#F34B7D", "H+", "#FFFFFF"),
    ".cc": ("#F34B7D", "CC", "#FFFFFF"),
    ".go": ("#00ADD8", "GO", "#FFFFFF"),
    ".rs": ("#DEA584", "RS", "#1F2328"),
    ".rb": ("#CC342D", "RB", "#FFFFFF"),
    ".php": ("#4F5D95", "PH", "#FFFFFF"),
    ".swift": ("#F05138", "SW", "#FFFFFF"),
    ".vue": ("#41B883", "VU", "#FFFFFF"),
    ".svelte": ("#FF3E00", "SV", "#FFFFFF"),
    ".dart": ("#00B4AB", "DT", "#FFFFFF"),
    ".lua": ("#000080", "LU", "#FFFFFF"),
    ".r": ("#198CE7", "R", "#FFFFFF"),
    ".pl": ("#0298C3", "PL", "#FFFFFF"),
    ".ex": ("#6E4A7E", "EX", "#FFFFFF"),
    ".exs": ("#6E4A7E", "ES", "#FFFFFF"),
    ".erl": ("#B83998", "ER", "#FFFFFF"),
    ".hs": ("#5E5086", "HS", "#FFFFFF"),
    ".clj": ("#63B132", "CL", "#FFFFFF"),
    ".scala": ("#DC322F", "SC", "#FFFFFF"),
    ".png": ("#A074C4", "PN", "#FFFFFF"),
    ".jpg": ("#A074C4", "JP", "#FFFFFF"),
    ".jpeg": ("#A074C4", "JP", "#FFFFFF"),
    ".gif": ("#A074C4", "GF", "#FFFFFF"),
    ".webp": ("#A074C4", "WP", "#FFFFFF"),
    ".bmp": ("#A074C4", "BM", "#FFFFFF"),
    ".ico": ("#A074C4", "IC", "#FFFFFF"),
    ".svg": ("#FFB13B", "SV", "#1F2328"),
    ".pdf": ("#D93831", "PD", "#FFFFFF"),
    ".zip": ("#E5C07B", "ZP", "#1F2328"),
    ".tar": ("#E5C07B", "TR", "#1F2328"),
    ".gz": ("#E5C07B", "GZ", "#1F2328"),
    ".7z": ("#E5C07B", "7Z", "#1F2328"),
    ".rar": ("#E5C07B", "RR", "#1F2328"),
    ".qss": ("#41ADFF", "QS", "#FFFFFF"),
    ".ui": ("#41ADFF", "UI", "#FFFFFF"),
    ".pro": ("#41ADFF", "PR", "#FFFFFF"),
    ".lock": ("#6A737D", "LK", "#FFFFFF"),
    ".gitignore": ("#F05032", "GI", "#FFFFFF"),
    ".gitattributes": ("#F05032", "GA", "#FFFFFF"),
    ".dockerignore": ("#2496ED", "DI", "#FFFFFF"),
    ".editorconfig": ("#FEFEFE", "ED", "#1F2328"),
}

_SPECIAL_NAMES: dict[str, tuple[str, str, str]] = {
    "dockerfile": ("#2496ED", "DK", "#FFFFFF"),
    "makefile": ("#6D8086", "MK", "#FFFFFF"),
    "cmakelists.txt": ("#064F8C", "CM", "#FFFFFF"),
    "requirements.txt": ("#3776AB", "PIP", "#FFFFFF"),
    "pipfile": ("#3776AB", "PIP", "#FFFFFF"),
    "pipfile.lock": ("#3776AB", "LK", "#FFFFFF"),
    "package.json": ("#CB3837", "NPM", "#FFFFFF"),
    "package-lock.json": ("#CB3837", "LK", "#FFFFFF"),
    "yarn.lock": ("#2C8EBB", "YR", "#FFFFFF"),
    "pnpm-lock.yaml": ("#F9AD00", "PN", "#1F2328"),
    "readme.md": ("#083FA1", "RM", "#FFFFFF"),
    "license": ("#D4AA00", "LC", "#1F2328"),
    "license.md": ("#D4AA00", "LC", "#1F2328"),
    "changelog.md": ("#083FA1", "CH", "#FFFFFF"),
    ".env": ("#ECD53F", "EN", "#1F2328"),
    ".env.example": ("#ECD53F", "EX", "#1F2328"),
    ".gitignore": ("#F05032", "GI", "#FFFFFF"),
    ".gitattributes": ("#F05032", "GA", "#FFFFFF"),
    ".editorconfig": ("#FEFEFE", "ED", "#1F2328"),
}


@lru_cache(maxsize=512)
def _badge_icon(cache_key: str, bg: str, label: str, fg: str = "#FFFFFF", size: int = 16) -> QIcon:
    del cache_key  # solo para la clave de caché
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    painter.setBrush(QColor(bg))
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawRoundedRect(0, 0, size - 1, size - 1, 3, 3)

    painter.setPen(QColor(fg))
    font = QFont("Sans Serif", 5 if len(label) > 2 else 6)
    font.setBold(True)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, label)
    painter.end()
    return QIcon(pixmap)


def explorer_icon_for_path(path: str) -> QIcon:
    """Devuelve un icono distintivo según el nombre o extensión del archivo."""
    base_name = os.path.basename(path)
    lower_name = base_name.lower()
    ext = os.path.splitext(lower_name)[1]

    if lower_name in _SPECIAL_NAMES:
        bg, label, fg = _SPECIAL_NAMES[lower_name]
        return _badge_icon(f"name:{lower_name}", bg, label, fg)

    if ext in _EXT_STYLES:
        bg, label, fg = _EXT_STYLES[ext]
        return _badge_icon(f"ext:{ext}", bg, label, fg)

    if ext:
        label = ext[1:].upper()[:3] or "?"
        return _badge_icon(f"ext:{ext}", "#6A737D", label, "#FFFFFF")

    return _icon_provider.icon(QFileIconProvider.IconType.File)


@lru_cache(maxsize=2)
def explorer_folder_icon(opened: bool = False) -> QIcon:
    del opened  # Qt 6 no define IconType.FolderOpen
    return _icon_provider.icon(QFileIconProvider.IconType.Folder)


def explorer_icon_size() -> QSize:
    return QSize(16, 16)
