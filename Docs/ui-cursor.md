# Interfaz estilo Cursor/VS Code

- [← Índice](./README.md)
- [Portada](../README.md)

## Layout
- **Activity Bar** (izquierda): Explorer / Search / Terminal / Settings
- **Sidebar**: pestañas **Explorer** y **Search**
- **Editor**: pestañas de archivos (indicador `•` si hay cambios sin guardar)
- **Panel inferior**: **Terminal**, **Problems** y ayuda
- **Status bar**: posición Ln/Col, tema activo y, si Pomodoro está activo, cuenta atrás `☕ MM:SS` hasta el próximo descanso
- **Barra superior**: botón **☕** para Modo Café (pausa manual; ver [Modo Café](./coffee-mode.md))

## Panels
- **Explorer**: árbol de archivos con **iconos por tipo** (Python, Markdown, JSON, imágenes, etc.) y raíz configurable
- **Search**: panel embebido con resultados clicables y reemplazo
- **Problems**: lista clicable de errores/warnings (salta a Ln/Col)

## Pestañas del editor

- **Nueva pestaña**: `Ctrl+T` o menú Archivo
- **Cerrar pestaña**: `Ctrl+W` o la ✕ de la pestaña
- **Cambios sin guardar**: al cerrar una pestaña modificada aparece un diálogo:
  - **Guardar** → guarda en el mismo archivo y cierra
  - **No** → descarta los cambios y cierra
  - **Cancelar** → mantiene la pestaña abierta

El título de la pestaña muestra un prefijo `•` mientras haya cambios pendientes de guardar.

## Markdown

Ver [Vista previa Markdown](./markdown.md).

