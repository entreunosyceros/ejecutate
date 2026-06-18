# 🐍 Ejecútate! — Editor de Código Python
<p align="center">
<img width="1024" height="1024" alt="logo" src="https://github.com/user-attachments/assets/53caa94d-580f-45ce-af56-6e312500e30d" />
<br/>

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![DeepWiki](https://img.shields.io/badge/DeepWiki-documentación-6366F1)](https://deepwiki.com/entreunosyceros/ejecutate)
</p>

Editor de código Python con arquitectura **MVC** e interfaz **PySide6**. Incluye terminal integrado, búsqueda avanzada, panel de problemas, temas personalizables, sistema educativo y utilidades para aprender Python sin morir en el intento.

**Ejecútate! no pretende sustituir a los grandes IDEs**. Su objetivo es ofrecer un entorno sencillo para aprender, experimentar y practicar Python sin tener que configurar herramientas complejas.

## ¿Para quién es?

- Personas que empiezan con Python.
- Estudiantes de cursos y certificados.
- Usuarios que quieren un entorno sencillo para practicar.
- Quien prefiera una herramienta ligera centrada en aprender.

## Inicio rápido

```bash
git clone https://github.com/entreunosyceros/ejecutate.git
cd ejecutate
python3 run_app.py
```

`run_app.py` se encarga de todo automáticamente:
- crea el entorno virtual `.venv` si no existe
- instala dependencias desde `requirements.txt` en la primera ejecución
- lanza la aplicación con el Python del venv

Si necesitas **reinstalar** dependencias manualmente: `python3 run_app.py --install-deps`

En caso de **ejecutar esta aplicación desde Windows**, recuerda que en ese S.O. python3 no funciona, utiliza python.

## Qué incluye

<img width="1917" height="1043" alt="ejecutate-editor" src="https://github.com/user-attachments/assets/8c7a4658-e2b5-4f32-a1cf-5fa36b74fc85" />

### Interfaz y edición
- Activity Bar, sidebar (**Explorer / Search / Problems / Outline / Aprendizaje**) y panel inferior (**Terminal / Problems / Características**)
- Barra superior con **carpeta de trabajo** visible junto al título
- Command Palette (`Ctrl+Shift+P`) y Quick Open (`Ctrl+P`)
- Menú **Archivo**: Nuevo, Abrir archivo, Abrir carpeta, Guardar, etc.
- Pestañas múltiples con aviso al cerrar si hay **cambios sin guardar**; la pestaña vacía inicial se reutiliza al abrir el primer archivo
- **Vista previa Markdown** opcional (`Ctrl+Shift+V`) en archivos `.md`
- Explorador con **iconos por tipo de archivo**, resaltado de sintaxis y panel **Problems** (sintaxis + avisos)
- **Outline** del archivo Python activo (clases y funciones con salto a línea)
- Varios temas (incluido **Café**) y **Modo Café** con Pomodoro opcional (descansos automáticos)
- **Preferencias** (`Ctrl+,`) con vista previa que respeta el tema activo (sin paneles ilegibles)

### Desarrollo
- Terminal integrado: ejecuta programas completos (`Ctrl+Enter`), caja inferior para `input()` y comandos manuales
- Selector de **intérprete** (solo shells instalados: Python, Bash, Sh/dash, Zsh, Fish…)
- Modos **Limpio** e **Interactivo** para la caja de comandos; precaptura de `input()`
- Formatter PEP 8 (autopep8 / black) y gestión de sesiones

### Aprendizaje (F4–F7)
- **Tutoriales interactivos (F4)**: 17 tutoriales en 4 niveles (Principiante → Experto), ordenados del más básico al más avanzado
- **Debugger visual (F5)**: ejecución paso a paso con inspección de variables
- **Gestor de paquetes (F6)**: catálogo de ~48 librerías habituales con filtro por categoría e instalación con un clic
- **Análisis de código (F7)**: sugerencias y avisos en tiempo real mientras escribes

También accesibles desde el panel **Aprendizaje** del sidebar. Detalle en [`Docs/education.md`](./Docs/education.md).

## Atajos más usados

| Atajo | Acción |
|-------|--------|
| `Ctrl+N` | Nuevo (pestaña vacía) |
| `Ctrl+O` | Abrir archivo |
| `Ctrl+Shift+O` | Abrir carpeta de trabajo |
| `Ctrl+P` | Quick Open (archivos recientes) |
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+Enter` | Ejecutar código en Terminal |
| `Ctrl+\`` | Alternar pestaña Terminal |
| `Ctrl+F` / `Ctrl+H` | Buscar / Buscar y reemplazar |
| `Ctrl+Shift+V` | Vista previa Markdown (solo `.md`) |
| `Ctrl+W` | Cerrar pestaña (avisa si hay cambios) |
| `Ctrl+Alt+C` | Modo Café (pausa manual o con Pomodoro) |
| `F4`–`F7` | Tutoriales / Debugger / Paquetes / Análisis |

Más atajos en [`Docs/shortcuts.md`](./Docs/shortcuts.md).

## Documentación completa

<img width="1136" height="814" alt="documentacion-ejecutate" src="https://github.com/user-attachments/assets/765df6d8-d67c-4752-ad25-dbe300238ff1" />

| Tema | Enlace |
|------|--------|
| Índice general | [`Docs/README.md`](./Docs/README.md) |
| Instalación y dependencias | [`Docs/install.md`](./Docs/install.md) |
| Interfaz del editor | [`Docs/editor-interface.md`](./Docs/editor-interface.md) |
| Archivos, pestañas y explorador | [`Docs/files-and-tabs.md`](./Docs/files-and-tabs.md) |
| Markdown y archivos `.txt` | [`Docs/markdown.md`](./Docs/markdown.md) |
| Búsqueda y reemplazo | [`Docs/search.md`](./Docs/search.md) |
| Terminal integrado | [`Docs/terminal.md`](./Docs/terminal.md) |
| Sistema educativo | [`Docs/education.md`](./Docs/education.md) |
| Arquitectura MVC | [`Docs/architecture.md`](./Docs/architecture.md) |
| Modo Café | [`Docs/coffee-mode.md`](./Docs/coffee-mode.md) |
| Añadir tutoriales | [`Docs/adding-tutorials.md`](./Docs/adding-tutorials.md) |
| **Wiki (DeepWiki)** | [deepwiki.com/entreunosyceros/ejecutate](https://deepwiki.com/entreunosyceros/ejecutate) |

## Licencia

**Ejecútate!** se distribuye bajo **[GNU GPL v3](LICENSE)**.

- **Estudios y uso personal:** puedes usarlo, estudiarlo y modificarlo con libertad.
- **Trabajo o proyectos propios:** también puedes usarlo; si **redistribuyes** el programa o versiones modificadas, debes respetar la GPL (código abierto, misma licencia, aviso de cambios). Consulta el archivo [`LICENSE`](LICENSE) para el texto legal completo.

## Dependencias principales

<img width="1918" height="1047" alt="preferencias-ejecutate" src="https://github.com/user-attachments/assets/9699f893-2444-40f1-aa04-9425137e58a1" />

PySide6 · Pygments · markdown · autopep8 · black · isort

---

🐍 **¡Ejecútate! — Básico pero coqueto** 🐍

*Desarrollado con pocas horas de sueño para la comunidad Python por entreunosyceros* ❤️
