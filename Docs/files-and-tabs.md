# Archivos, pestañas y explorador

- [← Índice](./README.md)
- [Portada](../README.md)

## Menú Archivo

Opciones disponibles en **📁 Archivo** (barra de menú superior):

| Opción | Atajo | Descripción |
|--------|-------|-------------|
| **Nuevo** | `Ctrl+N` | Crea una pestaña vacía sin guardar («Nuevo 1», «Nuevo 2», …) |
| **Abrir archivo…** | `Ctrl+O` | Abre `.py`, `.md`, `.txt` u otro archivo en el editor |
| **Abrir carpeta…** | `Ctrl+Shift+O` | Establece la carpeta de trabajo del explorador lateral |
| **Cerrar Pestaña** | `Ctrl+W` | Cierra la pestaña activa (avisa si hay cambios sin guardar) |
| **Guardar** | `Ctrl+S` | Guarda la pestaña actual |
| **Guardar Como…** | `Ctrl+Shift+S` | Guarda con otro nombre o ruta |
| **Salir** | `Ctrl+Q` | Cierra la aplicación |

Atajo alternativo para nueva pestaña vacía: `Ctrl+T`.

También disponible en **Command Palette** (`Ctrl+Shift+P`): *Nuevo*, *Abrir archivo…*, *Abrir carpeta…*.

## Pestañas del editor

### Pestaña inicial «Nuevo 1»

Al arrancar la aplicación se crea una pestaña vacía **Nuevo 1**. Si abres un archivo y esa pestaña sigue vacía (sin texto y sin cambios), **se reutiliza** en lugar de abrir otra pestaña: el título pasa a ser el nombre del archivo.

Si ya escribiste algo en «Nuevo 1» o hay cambios sin guardar, el archivo se abre en una **pestaña nueva**.

### Indicador de cambios

- Prefijo `•` en el título de la pestaña cuando hay modificaciones sin guardar.
- Al cerrar (`Ctrl+W` o ✕) aparece un diálogo: **Guardar** / **No** / **Cancelar**.

### Archivo ya abierto

Si el archivo ya está en otra pestaña, al abrirlo de nuevo solo se **activa** esa pestaña (no se duplica).

## Explorador de archivos (sidebar)

- **Doble clic** en un archivo → se abre en el editor (sin ventanas emergentes de confirmación).
- **Abrir carpeta** (menú Archivo o botón 📂 del explorador) → cambia la raíz del árbol de archivos.
- Iconos por tipo de extensión (Python, Markdown, JSON, imágenes, etc.).

## Carpeta de trabajo en la barra superior

Junto al título **Ejecútate!** se muestra la ruta de la carpeta raíz del explorador, por ejemplo:

`Ejecútate! — /home/usuario/proyectos/mi-app`

- Si la ruta es larga, se acorta por el centro; el **tooltip** muestra la ruta completa.
- El texto es **seleccionable** para copiarlo.
- Se actualiza al cambiar la carpeta de trabajo.

## Resaltado de sintaxis (Python)

En archivos `.py` el editor colorea:

- Palabras clave, funciones, clases
- **Cadenas** entre comillas (`"..."`, `'...'`, `"""..."""`)
- **Comentarios** `# ...` (cursiva y color distinto)
- Números y operadores

Los colores dependen del **tema** activo (Preferencias → Temas). El color base del texto no interfiere con el resaltado.

## Problems y Outline (sidebar)

- **Problems**: muestra errores/warnings del archivo actual y permite saltar a `Ln/Col`. El icono tiene un **badge** con el número de problemas.
- **Outline**: lista clases y funciones del archivo Python actual y permite saltar a la línea correspondiente.

## Ver también

- [Interfaz estilo Cursor](./ui-cursor.md)
- [Atajos de teclado](./shortcuts.md)
- [Modo Café y Pomodoro](./coffee-mode.md)
