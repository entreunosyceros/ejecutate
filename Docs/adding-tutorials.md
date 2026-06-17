# Añadir tutoriales

- [← Índice](./README.md)
- [Portada](../README.md)

Los tutoriales se definen en [`tutorials_config.py`](../tutorials_config.py) y los consume [`analyzers/tutorial_system.py`](../analyzers/tutorial_system.py).

## Estructura de un tutorial

```python
{
    'id': 'mi_tutorial',           # identificador único (snake_case)
    'title': 'Título visible',
    'description': 'Resumen breve',
    'difficulty': 'Principiante',  # ver niveles abajo
    'sort_order': 5,               # orden dentro del mismo nivel (menor = antes)
    'steps': [
        {
            'title': 'Nombre del paso',
            'content': 'Explicación (puede ser multilínea)',
            'code_example': 'print("ejemplo")',
            'expected_output': 'ejemplo',
            'validation_contains': ['print'],  # tokens que debe incluir el código del usuario
            'hints': ['Pista 1', 'Pista 2'],
        },
        # más pasos...
    ],
}
```

## Niveles de dificultad

Usa exactamente uno de estos valores (definen el orden en el diálogo F4):

| Valor | Orden | Uso |
|-------|-------|-----|
| `Principiante` | 1 | Sintaxis básica, variables, estructuras simples |
| `Intermedio` | 2 | Archivos, excepciones, módulos, comprensiones |
| `Avanzado` | 3 | POO, herencia, generadores, context managers |
| `Experto` | 4 | Decoradores, async, typing, patrones avanzados |

Los tutoriales se listan primero por nivel (básico → experto) y luego por `sort_order`.

## Validación de código

Cada paso puede definir `validation_contains`: lista de cadenas que el código del usuario debe incluir (comparación sin distinguir mayúsculas).

La función `validate_tutorial_code()` en `tutorials_config.py` comprueba esos tokens automáticamente. Si falla, muestra la primera pista del paso.

## Pasos para añadir uno nuevo

1. Abre `tutorials_config.py`.
2. Añade un diccionario al final de la lista en `get_tutorials_config()`.
3. Asigna `difficulty` y `sort_order` coherentes con el resto del catálogo.
4. Define al menos un paso con `validation_contains` acorde al ejercicio.
5. Reinicia la app o vuelve a abrir el diálogo F4 para ver el tutorial.

## Consejos

- Mantén los ejemplos **pequeños y ejecutables**.
- Usa `validation_contains` con tokens inequívocos (`async`, `yield`, `@dataclass`).
- Agrupa temas relacionados en el mismo nivel antes de subir de dificultad.
- Actualiza [`Docs/education.md`](./education.md) si añades un tutorial destacado o cambias la estructura por niveles.
