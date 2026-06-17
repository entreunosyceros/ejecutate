# Instalación y ejecución

- [← Índice](./README.md)
- [Portada](../README.md)

## Requisitos
- Python 3
- Conexión a internet (solo la primera vez, para instalar dependencias)

## Instalación rápida

```bash
git clone https://github.com/sapoclay/ejecutate.git
cd ejecutate
python3 run_app.py
```

No hace falta ejecutar ningún comando extra: `run_app.py` crea `.venv` e instala dependencias automáticamente en la primera ejecución.

## Qué hace `run_app.py`

1. Crea el entorno virtual `.venv` si no existe
2. Instala dependencias desde `requirements.txt` (solo cuando el venv es nuevo)
3. Ejecuta la aplicación con el Python del venv

## Reinstalar dependencias

Si cambias `requirements.txt` o algo falla al importar PySide6:

```bash
python3 run_app.py --install-deps
```

O recrea el entorno desde cero:

```bash
rm -rf .venv
python3 run_app.py
```

## Dependencias principales
- **PySide6**: interfaz gráfica
- **Pygments**: resaltado de sintaxis
- **autopep8 / black**: formateo
- **isort**: organización de imports

## Verificar dependencias (alternativa)

```bash
python3 main.py --check-deps
```
