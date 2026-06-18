# Terminal integrado

- [← Índice](./README.md)
- [Portada](../README.md)

El terminal integrado (`utils/new_terminal.py`) permite ejecutar comandos y Python dentro de la app.

## Botón «Ejecutar Código» (editor)

**Siempre ejecuta el programa completo** en el shell integrado (Bash), igual que en una terminal:

1. Si el archivo está **guardado** → `cd carpeta && python archivo.py`
2. Si la pestaña **no está guardada** → se crea un `.py` temporal y se ejecuta entero
3. La salida aparece arriba; si el programa **pide datos** (menús, `input()`, Rich, Textual…), escríbelos en la **caja inferior** del terminal y pulsa Enter

Antes de ejecutar, si hay cambios sin guardar en un archivo con ruta, se guarda automáticamente.

### Código con `input()` y precaptura

Si activas **«Precapturar inputs»**, se muestra un diálogo para rellenar los `input()` antes de lanzar el programa (útil en scripts simples, no en TUIs completas).

## Intérprete del terminal

El desplegable **Intérprete** solo muestra shells instalados en el equipo donde corre Ejecútate! (Python del venv, bash, sh, zsh, fish…). Los que no existan no aparecen en la lista.

La **caja inferior** envía comandos al intérprete activo.

## Caja de comandos del terminal (manual)

Los controles **Limpio / Interactivo** y **Auto-detect** solo afectan a lo que escribes tú en la caja inferior del terminal, no al botón del editor.

- **Limpio**: subprocess, solo stdout/stderr
- **Interactivo**: REPL embebido (`python -i`) para pruebas rápidas a mano

## Detección y precaptura

- **Precapturar inputs**: recolecta valores de `input()` antes de ejecutar desde el editor
