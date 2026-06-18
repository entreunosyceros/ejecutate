# Terminal integrado

- [← Índice](./README.md)
- [Portada](../README.md)

El terminal integrado (`utils/new_terminal.py`) permite ejecutar comandos y Python dentro de la app.

## Botón «Ejecutar Código» (editor)

**Siempre ejecuta el programa completo** en el shell integrado (normalmente Bash), igual que en una terminal:

1. Si el archivo está **guardado** → `cd carpeta && python archivo.py`
2. Si la pestaña **no está guardada** → se crea un `.py` temporal y se ejecuta entero
3. La salida aparece arriba; si el programa **pide datos** (menús, `input()`, Rich, Textual…), escríbelos en la **caja inferior** del terminal y pulsa Enter

Antes de ejecutar, si hay cambios sin guardar en un archivo con ruta, se guarda automáticamente.

### Código con `input()` y precaptura

Si activas **«Precapturar inputs»**, se muestra un diálogo para rellenar los `input()` antes de lanzar el programa (útil en scripts simples, no en TUIs completas).

## Intérprete del terminal

El desplegable **🖥️ Intérprete** lista **solo shells instalados** en el equipo (detectados con `PATH`):

| Intérprete | Uso habitual |
|------------|----------------|
| **Python** | REPL interactivo (`python -i`) |
| **Bash** | Comandos de sistema, ejecutar `.py` con `python3 script.py` |
| **Sh (dash)** | Shell POSIX mínima en muchas distros Linux (`/bin/sh` → dash) |
| **Zsh / Fish** | Aparecen si están instalados |

- Los que **no existan** en tu sistema **no se muestran** en la lista.
- **🔄 Reiniciar** vuelve a escanear intérpretes disponibles (útil tras instalar zsh o fish).
- En Linux, **Sh** suele ser **dash** (etiqueta «Sh (dash)»). Dash no usa el flag `-i` de bash; la app lo gestiona automáticamente.

La **caja inferior** envía comandos al intérprete activo.

## Caja de comandos del terminal (manual)

Los controles **Limpio / Interactivo**, **Auto-detect** y **Precapturar inputs** solo afectan a lo que escribes tú en la caja inferior, **no** al botón «Ejecutar Código» del editor.

- **Limpio**: subprocess, solo stdout/stderr
- **Interactivo**: REPL embebido (`python -i`) para pruebas rápidas a mano

## Controles de la barra del terminal

- **🗑️ Limpiar**: borra la salida visible
- **🔄 Reiniciar**: reinicia el shell y actualiza la lista de intérpretes
- **Terminal del sistema** (`Ctrl+Alt+T`): terminal nativa del SO (recomendada para TUIs a pantalla completa)

## Errores de ejecución

Los errores al **ejecutar** un programa aparecen en el **Terminal**, no en el panel **Problems** (este último es para sintaxis y avisos estáticos del código).
