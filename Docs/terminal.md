# Terminal integrado

- [← Índice](./README.md)
- [Portada](../README.md)

El terminal integrado (`utils/new_terminal.py`) permite ejecutar comandos y Python de forma interactiva dentro de la app.

## Modos
- **Limpio**: ejecuta en subprocess y muestra stdout/stderr
- **Interactivo**: envía el código al REPL embebido

## Detección y precaptura
- **Auto-detect**: detecta código con `input()`/`getpass()` y cambia de modo
- **Precapturar inputs**: recolecta valores antes de ejecutar para evitar bloqueos

