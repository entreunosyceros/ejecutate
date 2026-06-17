# Sistema educativo (F4–F7)

- [← Índice](./README.md)
- [Portada](../README.md)

Herramientas de aprendizaje accesibles con **F4–F7**, desde el menú **Educación** o desde el panel **Aprendizaje** del sidebar.

## Tutoriales interactivos (F4)

Sistema modular configurado en [`tutorials_config.py`](../tutorials_config.py). El diálogo muestra los tutoriales **agrupados por nivel**, del más básico al más experto.

### Niveles

| Nivel | Tutoriales |
|-------|------------|
| 🟢 **Principiante** | Primeros pasos con Python · Strings y texto · Diccionarios · Estructuras de control |
| 🟡 **Intermedio** | Listas y funciones · Tuplas y conjuntos · Archivos · Errores · Módulos · Comprensiones |
| 🟠 **Avanzado** | POO · Herencia · Context managers · Generadores |
| 🔴 **Experto** | Decoradores · Async/await · Type hints y dataclasses |

**Total: 17 tutoriales** con pasos guiados, ejemplos de código, pistas y verificación del código que escribes.

### Cómo usarlos

1. Pulsa **F4** o el botón **Tutoriales** en el panel Aprendizaje.
2. Elige un tutorial (empieza por los de nivel principiante).
3. Sigue los pasos, escribe código en el área de práctica y pulsa **Verificar**.
4. Avanza con **Siguiente** hasta completar el tutorial.

Para añadir o modificar tutoriales: [Añadir tutoriales](./adding-tutorials.md).

## Debugger visual (F5)

- Ejecución **paso a paso** del código del editor
- Inspección de **variables** y valores en tiempo real
- Captura de la **salida** del programa
- Útil para entender qué hace cada línea antes de pasar a temas más avanzados

## Gestor de paquetes (F6)

Instala y explora librerías Python sin usar la terminal manualmente.

### Catálogo (~48 paquetes en 16 categorías)

| Categoría | Ejemplos |
|-----------|----------|
| Web | `requests`, `httpx`, `beautifulsoup4`, `selenium`, `aiohttp` |
| Web framework | `flask`, `django`, `fastapi`, `uvicorn`, `starlette` |
| Datos | `pandas`, `numpy`, `openpyxl`, `pyyaml`, `xlrd` |
| Visualización | `matplotlib`, `seaborn`, `plotly` |
| Ciencia | `scipy`, `scikit-learn` |
| GUI | `PySide6`, `customtkinter` |
| Terminal / TUI | `rich`, `textual`, `click`, `typer` |
| Imágenes | `pillow`, `opencv-python` |
| Juegos | `pygame` |
| Datos y persistencia | `sqlalchemy` (ORM), `pymongo` (cliente MongoDB), `psycopg2-binary` (driver PostgreSQL) |
| Desarrollo | `pytest`, `black`, `ruff`, `mypy`, `autopep8`, `ipython` |
| Utilidades | `python-dotenv`, `tqdm`, `schedule` |
| Seguridad | `cryptography`, `bcrypt` |
| Documentos / PDF | `python-docx`, `pypdf` |

La categoría **Datos y persistencia** agrupa ORM, drivers y clientes de bases de datos (no confundir con **Datos**, orientada a análisis y tablas con pandas/numpy).

### Funciones del diálogo

- **Filtro por categoría** en el catálogo
- **Detalle** de cada paquete con descripción y ejemplos
- **Instalación con pip** en segundo plano (log de progreso)
- Pestaña de **paquetes ya instalados**

Configuración del catálogo: [`analyzers/package_manager.py`](../analyzers/package_manager.py).

## Análisis de código (F7)

- Subrayado y recomendaciones **en tiempo real** mientras escribes
- Complementa el panel **Problems** (errores de sintaxis con debounce)
- Sugerencias de estilo, f-strings, bucles potencialmente infinitos, etc.

## Ruta de aprendizaje sugerida

1. Activa el análisis (**F7**) para feedback inmediato.
2. Completa los tutoriales de **principiante** (**F4**).
3. Practica en el editor y usa el **debugger** (**F5**) cuando algo no cuadre.
4. Instala librerías que necesites con el **gestor de paquetes** (**F6**).
5. Sigue con tutoriales **intermedio → avanzado → experto** según tu ritmo.
