# Política de seguridad

## Versiones con soporte

| Versión | Soportada |
| ------- | --------- |
| `main` (desarrollo activo) | ✅ |
| Versiones etiquetadas en releases | ✅ mientras no se indique lo contrario |

## Alcance

**Ejecútate!** es una aplicación de escritorio (PySide6) que ejecuta código Python en un terminal integrado y puede abrir terminales del sistema operativo. En el ámbito de seguridad nos interesa especialmente:

- Ejecución de código o comandos no previstos al abrir archivos, proyectos o entradas del terminal integrado.
- Inyección de comandos al invocar shells externos (`open_system_terminal`, REPL, modo interactivo).
- Lectura o escritura de archivos fuera del directorio esperado por el explorador o la gestión de sesiones.
- Dependencias con vulnerabilidades conocidas en `requirements.txt`.
- Fugas de datos sensibles en `.editor_session.json` o logs locales.

**Fuera de alcance habitual:** fallos de red al instalar paquetes con `pip`, comportamiento de terminales del sistema operativo, o código malicioso que el usuario ejecute deliberadamente en el terminal integrado.

## Cómo reportar una vulnerabilidad

1. **No** abras un issue público con detalles del fallo de seguridad.
2. Usa [GitHub Security Advisories](https://github.com/entreunosyceros/ejecutate/security/advisories/new) (**Report a vulnerability**) si la opción está habilitada en este repositorio.
3. Si no puedes usar Advisories, abre un issue con el título `SECURITY (sin detalles)` y solicita un canal privado; no incluyas pasos de explotación en el tablón público.

Incluye, en la medida de lo posible:

- Descripción del problema y componente afectado (p. ej. `utils/new_terminal.py`, explorador de archivos).
- Pasos detallados para reproducir el fallo.
- Impacto estimado (local, otros usuarios del mismo equipo).
- Versión de Python, SO y commit afectado.
- Sugerencia de mitigación, si dispones de ella.

## Qué esperar

- **Acuse de recibo:** evaluación inicial en un plazo razonable de pocos días.
- **Resolución:** parche o mitigación en una versión posterior si procede.
- **Créditos:** reconocimiento al informante en las notas de la release, salvo que se solicite anonimato.

## Buenas prácticas para usuarios

- Ejecuta el editor con `python3 run_app.py` desde el [repositorio oficial](https://github.com/entreunosyceros/ejecutate).
- No ejecutes código de fuentes no confiables en el terminal integrado sin revisarlo.
- Mantén Python y las dependencias actualizadas: `python3 run_app.py --install-deps`.
- No compartas `.editor_session.json` si contiene rutas o fragmentos de código que consideres privados.
