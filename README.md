# 🐍 Ejecútalo! — Editor de Código Python

<img width="1024" height="1024" alt="logo" src="https://github.com/user-attachments/assets/53caa94d-580f-45ce-af56-6e312500e30d" />

Editor de código Python con arquitectura **MVC** e interfaz **PySide6**. Incluye terminal integrado, búsqueda avanzada, panel de problemas, temas personalizables, sistema educativo y utilidades para aprender Python sin morir en el intento.

## Inicio rápido

```bash
git clone https://github.com/sapoclay/ejecutate.git
cd ejecutate
python3 run_app.py
```

`run_app.py` se encarga de todo automáticamente:
- crea el entorno virtual `.venv` si no existe
- instala dependencias desde `requirements.txt` en la primera ejecución
- lanza la aplicación con el Python del venv

Si necesitas **reinstalar** dependencias manualmente: `python3 run_app.py --install-deps`

## Qué incluye

### Interfaz y edición
- Activity Bar, sidebar (**Explorer / Search**) y panel inferior (**Terminal / Problems**)
- Command Palette (`Ctrl+Shift+P`) y Quick Open (`Ctrl+P`)
- Pestañas múltiples, resaltado de sintaxis y verificación en tiempo real
- Explorador de archivos, autocompletado y varios temas (incluido **Café**)

### Desarrollo
- Terminal integrado con modos **Limpio** e **Interactivo**
- Auto-detección de `input()` y precaptura de entradas
- Formatter PEP 8 (autopep8 / black) y gestión de sesiones

### Aprendizaje (F4–F7)
- Tutoriales interactivos, debugger visual, gestor de paquetes y analizador de código

## Atajos más usados

| Atajo | Acción |
|-------|--------|
| `Ctrl+P` | Quick Open (archivos recientes) |
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+Enter` | Ejecutar código en Terminal |
| `Ctrl+\`` | Alternar pestaña Terminal |
| `Ctrl+F` / `Ctrl+H` | Buscar / Buscar y reemplazar |
| `Ctrl+Alt+C` | Modo Café (pausa) |
| `F4`–`F7` | Tutoriales / Debugger / Paquetes / Análisis |

Más atajos en [`Docs/shortcuts.md`](./Docs/shortcuts.md).

## Documentación completa

| Tema | Enlace |
|------|--------|
| Índice general | [`Docs/README.md`](./Docs/README.md) |
| Instalación y dependencias | [`Docs/install.md`](./Docs/install.md) |
| Interfaz estilo Cursor | [`Docs/ui-cursor.md`](./Docs/ui-cursor.md) |
| Búsqueda y reemplazo | [`Docs/search.md`](./Docs/search.md) |
| Terminal integrado | [`Docs/terminal.md`](./Docs/terminal.md) |
| Sistema educativo | [`Docs/education.md`](./Docs/education.md) |
| Arquitectura MVC | [`Docs/architecture.md`](./Docs/architecture.md) |
| Modo Café | [`Docs/coffee-mode.md`](./Docs/coffee-mode.md) |
| Añadir tutoriales | [`Docs/adding-tutorials.md`](./Docs/adding-tutorials.md) |

## Dependencias principales

PySide6 · Pygments · autopep8 · black · isort

---

🐍 **¡Editor de Python Ejecútate! — Básico pero coqueto** 🐍

*Desarrollado con pocas horas de sueño para la comunidad Python por entreunosyceros* ❤️
