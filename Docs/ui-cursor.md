# Interfaz estilo Cursor/VS Code

- [← Índice](./README.md)
- [Portada](../README.md)

## Layout

- **Barra superior**: título **Ejecútalo!**, ruta de la carpeta de trabajo del explorador y botón **☕** (Modo Café)
- **Activity Bar** (izquierda): Explorer / Search / Problems / Outline / Aprendizaje / Terminal / Settings
- **Sidebar**: pestañas **Explorer**, **Search**, **Problems**, **Outline** y **Aprendizaje**
- **Editor**: pestañas de archivos (indicador `•` si hay cambios sin guardar)
- **Panel inferior**: **Terminal**, **Problems** y ayuda; se puede cerrar con **✕** o desde **Vista → Panel inferior** (`Ctrl+` `)
- **Status bar**: posición Ln/Col, tema activo y, si Pomodoro está activo, cuenta atrás `☕ MM:SS` hasta el próximo descanso

## Menú Archivo

| Opción | Atajo |
|--------|-------|
| Nuevo | `Ctrl+N` |
| Abrir archivo… | `Ctrl+O` |
| Abrir carpeta… | `Ctrl+Shift+O` |
| Cerrar Pestaña | `Ctrl+W` |
| Guardar | `Ctrl+S` |
| Guardar Como… | `Ctrl+Shift+S` |
| Salir | `Ctrl+Q` |

Detalle del comportamiento de pestañas y explorador: [Archivos, pestañas y explorador](./files-and-tabs.md).

## Panels

- **Explorer**: árbol de archivos con **iconos por tipo** (Python, Markdown, JSON, imágenes, etc.) y raíz configurable. Doble clic abre el archivo en el editor.
- **Search**: panel embebido con resultados clicables y reemplazo
- **Problems**: lista clicable de errores/warnings (salta a Ln/Col) + contador (badge) en el icono
- **Outline**: símbolos del archivo Python (clases/funciones) con salto a línea
- **Aprendizaje**: accesos a Tutoriales/Debugger/Paquetes/Análisis (F4–F7)

## Pestañas del editor

- **Nuevo**: `Ctrl+N` (o `Ctrl+T`) o menú **Archivo → Nuevo**
- **Abrir archivo**: explorador (doble clic), `Ctrl+O` o **Archivo → Abrir archivo…**
- **Cerrar pestaña**: `Ctrl+W` o la ✕ de la pestaña
- **Pestaña vacía inicial**: al abrir el primer archivo, «Nuevo 1» se sustituye por la pestaña del archivo si sigue vacía
- **Cambios sin guardar**: al cerrar una pestaña modificada aparece un diálogo:
  - **Guardar** → guarda en el mismo archivo y cierra
  - **No** → descarta los cambios y cierra
  - **Cancelar** → mantiene la pestaña abierta

El título de la pestaña muestra un prefijo `•` mientras haya cambios pendientes de guardar.

## Resaltado de sintaxis

En Python, cadenas entre comillas y comentarios `#` usan colores distintos al texto normal. Los colores se configuran con el tema en Preferencias.

## Panel inferior

- **Vista → Panel inferior** o `Ctrl+` `: muestra u oculta el panel (Terminal, Problems, Características)
- Botón **✕** en la cabecera del panel: cierra el panel
- Al cerrar el panel, el **Editor** ocupa todo el alto disponible
- Al ejecutar código (`Ctrl+Enter`) el panel se abre automáticamente en la pestaña Terminal

## Markdown

Ver [Vista previa Markdown](./markdown.md).

## Modo Café

Ver [Modo Café y Pomodoro](./coffee-mode.md).
