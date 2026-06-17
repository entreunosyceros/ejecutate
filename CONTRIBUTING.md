# Guía de contribución

¡Gracias por interesarte en **Ejecútate!** — editor de código Python con interfaz PySide6, terminal integrado, sistema educativo y documentación en [`Docs/`](Docs/README.md). Cualquier mejora bien planteada es bienvenida.

Repositorio oficial: https://github.com/entreunosyceros/ejecutate

## Antes de empezar

- Lee el [README](README.md) y el [índice de documentación](Docs/README.md).
- Revisa las [issues abiertas](https://github.com/entreunosyceros/ejecutate/issues) por si alguien ya trabaja en lo mismo.
- Consulta el [Código de conducta](CODE_OF_CONDUCT.md).
- Para vulnerabilidades, sigue [SECURITY.md](SECURITY.md) (no abras issues públicas con detalles de explotación).

## Cómo puedes ayudar

- **Reportar errores** en el editor, terminal integrado, explorador, vista previa Markdown, debugger o tutoriales.
- **Proponer mejoras** de interfaz, atajos, rendimiento o experiencia de aprendizaje.
- **Enviar pull requests** acotados y probados manualmente en Linux (y en Windows/macOS si puedes).
- **Mejorar documentación** (README, `Docs/`, textos de la interfaz, F2).
- **Añadir o mejorar tutoriales** — ver [Docs/adding-tutorials.md](Docs/adding-tutorials.md).

## Entorno de desarrollo

Requisitos: **Python 3** (se recomienda 3.10+).

```bash
git clone https://github.com/entreunosyceros/ejecutate.git
cd ejecutate
python3 run_app.py
```

`run_app.py` crea el entorno virtual `.venv` e instala dependencias en la primera ejecución.

### Reinstalar dependencias

```bash
python3 run_app.py --install-deps
```

### Arranque manual (opcional)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
.venv/bin/python main.py
```

## Áreas del código

| Área | Ubicación habitual |
|------|-------------------|
| Vista principal / UI | `views/editor_view.py` |
| Controlador MVC | `controllers/editor_controller.py` |
| Ejecución de código | `models/code_executor.py` |
| Terminal integrado | `utils/new_terminal.py` |
| Vista previa Markdown | `utils/markdown_preview.py` |
| Iconos del explorador | `utils/file_icons.py` |
| Debugger / tutoriales / análisis | `analyzers/` |
| Configuración y temas | `config.py` |
| Estilos globales | `styles/cursor_dark.qss` |
| Documentación | `Docs/` |

## Estilo de código

- Sigue el estilo del código existente (nombres, imports, nivel de comentarios).
- Cambios **mínimos y enfocados**: no mezcles varias funcionalidades en un mismo PR.
- Los textos visibles para el usuario van en **español**.
- No incluyas secretos, `.editor_session.json` personal ni `__pycache__/` en commits.
- No subas archivos generados accidentalmente (p. ej. `=3.4.0` por un `pip` mal escrito).

## Pull requests

1. Crea una rama descriptiva desde `main` (por ejemplo `fix/tab-close-save` o `feat/markdown-preview`).
2. Describe **qué** cambias y **por qué**.
3. Indica cómo lo has probado (pasos manuales, capturas o SO usado).
4. Actualiza `Docs/` o el README solo si el cambio lo requiere.

Usa la [plantilla de pull request](.github/pull_request_template.md) al abrir el PR.

## Reportar problemas

- **Bugs y mejoras:** [plantillas de GitHub Issues](https://github.com/entreunosyceros/ejecutate/issues/new/choose).
- **Seguridad:** [SECURITY.md](SECURITY.md).

## Licencia

Al contribuir, aceptas que tu aportación se publique bajo la misma licencia del proyecto: [GPL-3.0](LICENSE).
