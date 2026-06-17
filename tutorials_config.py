#!/usr/bin/env python3
"""
Configuración de tutoriales independiente
Archivo para gestionar todos los tutoriales de manera sencilla
"""

from typing import List, Dict, Any

DIFFICULTY_ORDER = {
    'Principiante': 1,
    'Intermedio': 2,
    'Avanzado': 3,
    'Experto': 4,
}

DIFFICULTY_HEADERS = {
    'Principiante': '🟢 Nivel principiante',
    'Intermedio': '🟡 Nivel intermedio',
    'Avanzado': '🟠 Nivel avanzado',
    'Experto': '🔴 Nivel experto',
}


def get_difficulty_order(difficulty: str) -> int:
    """Orden numérico de dificultad (menor = más básico)."""
    return DIFFICULTY_ORDER.get(difficulty, 99)


def get_tutorials_config() -> List[Dict[str, Any]]:
    """
    Configuración de todos los tutoriales disponibles
    
    Para añadir un nuevo tutorial:
    1. Añade un nuevo diccionario a la lista
    2. Define los pasos con su contenido
    3. Especifica la validación si es necesaria
    
    Returns:
        List[Dict]: Lista de configuraciones de tutoriales
    """
    return [
        # Tutorial 1: Primeros pasos con Python
        {
            'id': 'python_basics',
            'title': 'Primeros pasos con Python',
            'description': 'Aprende lo básico de Python: variables, tipos de datos y operaciones simples',
            'difficulty': 'Principiante',
            'sort_order': 1,
            'steps': [
                {
                    'title': 'Bienvenido a Python',
                    'content': '''¡Hola! Bienvenido a tu primer tutorial de Python.
                    
Python es un lenguaje de programación muy popular y fácil de aprender. Es perfecto para principiantes porque:

• **Sintaxis simple**: Se lee casi como inglés
• **Muy potente**: Puedes hacer desde páginas web hasta inteligencia artificial
• **Gran comunidad**: Millones de programadores te pueden ayudar

¡Empecemos con tu primera línea de código!''',
                    'code_example': 'print("¡Hola, mundo!")',
                    'expected_output': '¡Hola, mundo!',
                    'validation_contains': ['print'],
                    'hints': [
                        'La función print() muestra texto en la pantalla',
                        'El texto debe ir entre comillas ("texto")',
                        'No olvides cerrar el paréntesis'
                    ]
                },
                {
                    'title': 'Variables y números',
                    'content': '''Excelente! Ahora aprenderás sobre **variables**.

Las variables son como cajas donde guardas información:

• **Números enteros**: `edad = 25`
• **Números decimales**: `altura = 1.75`
• **Texto**: `nombre = "Ana"`

Python es inteligente y detecta automáticamente qué tipo de dato estás guardando.''',
                    'code_example': '''edad = 25
nombre = "Ana"
print("Mi nombre es", nombre, "y tengo", edad, "años")''',
                    'expected_output': 'Mi nombre es Ana y tengo 25 años',
                    'validation_contains': ['=', 'print'],
                    'hints': [
                        'Usa = para asignar valores a variables',
                        'Los nombres van entre comillas',
                        'Los números van sin comillas',
                        'Puedes mostrar varias cosas con print separándolas por comas'
                    ]
                },
                {
                    'title': 'Operaciones matemáticas',
                    'content': '''¡Genial! Ahora aprenderás operaciones matemáticas básicas.

Python puede hacer matemáticas como una calculadora:

• **Suma**: `+`
• **Resta**: `-`
• **Multiplicación**: `*`
• **División**: `/`

También puedes usar paréntesis para cambiar el orden de las operaciones.''',
                    'code_example': '''numero1 = 10
numero2 = 5
suma = numero1 + numero2
print("La suma es:", suma)
print("La multiplicación es:", numero1 * numero2)''',
                    'expected_output': '''La suma es: 15
La multiplicación es: 50''',
                    'validation_contains': ['+', 'print'],
                    'hints': [
                        'Usa + para sumar números',
                        'Puedes guardar el resultado en una variable',
                        'Recuerda que * significa multiplicación',
                        'Puedes hacer varias operaciones en una línea'
                    ]
                },
                {
                    'title': 'Pidiendo información al usuario',
                    'content': '''¡Muy bien! Ahora aprenderás a pedir información al usuario.

La función `input()` te permite pedir al usuario que escriba algo:

• **input()**: Pide texto al usuario
• **int()**: Convierte texto a número entero
• **float()**: Convierte texto a número decimal

¡Esto hace que tus programas sean interactivos!''',
                    'code_example': '''nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
print("Hola", nombre + ", tienes", edad, "años")''',
                    'expected_output': '''¿Cómo te llamas? Juan
¿Cuántos años tienes? 20
Hola Juan, tienes 20 años''',
                    'validation_contains': ['input', 'print'],
                    'hints': [
                        'input() siempre devuelve texto',
                        'Puedes poner una pregunta dentro de input()',
                        'Para unir texto usa el símbolo +'
                    ]
                }
            ]
        },
        
        # Tutorial 2: Estructuras de control
        {
            'id': 'control_structures',
            'title': 'Estructuras de control',
            'description': 'Aprende a usar if, else, for y while para controlar el flujo de tu programa',
            'difficulty': 'Principiante',
            'sort_order': 4,
            'steps': [
                {
                    'title': 'Decisiones con if',
                    'content': '''Ahora aprenderás a tomar decisiones en tu programa.

La estructura `if` ejecuta código solo si una condición es verdadera:

• **if**: Si la condición es verdadera, ejecuta el código
• **else**: Si no, ejecuta este otro código
• **elif**: Si hay más opciones

¡Es como decir "si pasa esto, haz aquello"!''',
                    'code_example': '''edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")''',
                    'expected_output': 'Eres mayor de edad',
                    'validation_contains': ['if', 'print'],
                    'hints': [
                        'Usa >= para "mayor o igual que"',
                        'No olvides los dos puntos : después del if',
                        'El código después del if debe estar indentado',
                        'else se ejecuta cuando if es falso'
                    ]
                },
                {
                    'title': 'Múltiples opciones con elif',
                    'content': '''¡Excelente! Ahora aprenderás a manejar múltiples opciones.

Con `elif` puedes verificar varias condiciones:

• **if**: Primera condición
• **elif**: Segunda condición (y más...)
• **else**: Si ninguna es verdadera

¡Es como tener un menú de opciones!''',
                    'code_example': '''nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bien")
else:
    print("Necesitas estudiar más")''',
                    'expected_output': 'Bien',
                    'validation_contains': ['if', 'elif', 'print'],
                    'hints': [
                        'elif significa "else if" (sino si)',
                        'Puedes tener varios elif',
                        'Solo se ejecuta el primer caso verdadero',
                        'Siempre indenta el código después de :'
                    ]
                },
                {
                    'title': 'Bucles con for',
                    'content': '''¡Genial! Ahora aprenderás a repetir código automáticamente.

El bucle `for` repite código un número específico de veces:

• **range(5)**: Números del 0 al 4
• **range(1, 6)**: Números del 1 al 5
• **for**: Repite para cada elemento

¡Es perfecto para tareas repetitivas!''',
                    'code_example': '''print("Contando del 1 al 5:")
for numero in range(1, 6):
    print("Número:", numero)
print("¡Terminé de contar!")''',
                    'expected_output': '''Contando del 1 al 5:
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
¡Terminé de contar!''',
                    'validation_contains': ['for', 'range', 'print'],
                    'hints': [
                        'range(1, 6) va del 1 al 5 (no incluye el 6)',
                        'La variable numero toma cada valor del rango',
                        'Indenta el código que quieres repetir',
                        'for in range() es muy común en Python'
                    ]
                },
                {
                    'title': 'Bucles con while',
                    'content': '''¡Muy bien! Ahora aprenderás otro tipo de bucle.

El bucle `while` repite mientras una condición sea verdadera:

• **while**: Mientras la condición sea verdadera
• **Cuidado**: Asegúrate de que la condición cambie
• **Infinito**: Si no cambia, el bucle nunca para

¡Es útil cuando no sabes cuántas veces repetir!''',
                    'code_example': '''contador = 1
while contador <= 3:
    print("Vuelta número:", contador)
    contador = contador + 1
print("Bucle terminado")''',
                    'expected_output': '''Vuelta número: 1
Vuelta número: 2
Vuelta número: 3
Bucle terminado''',
                    'validation_contains': ['while', 'print'],
                    'hints': [
                        'while continúa mientras la condición sea verdadera',
                        'Siempre modifica la variable del while',
                        'contador = contador + 1 se puede escribir como contador += 1',
                        'Si no cambias contador, el bucle será infinito'
                    ]
                }
            ]
        },
        
        # Tutorial 3: Listas y funciones
        {
            'id': 'lists_functions',
            'title': 'Listas y funciones',
            'description': 'Aprende a trabajar con listas y crear tus propias funciones',
            'difficulty': 'Intermedio',
            'sort_order': 1,
            'steps': [
                {
                    'title': 'Trabajando con listas',
                    'content': '''¡Hola de nuevo! Ahora aprenderás sobre **listas**.

Las listas te permiten guardar varios elementos en una sola variable:

• **Crear lista**: `numeros = [1, 2, 3]`
• **Agregar**: `lista.append(elemento)`
• **Acceder**: `lista[0]` (primer elemento)
• **Longitud**: `len(lista)`

¡Es como tener una caja con compartimentos!''',
                    'code_example': '''frutas = ["manzana", "banana", "naranja"]
print("Mis frutas:", frutas)
print("Primera fruta:", frutas[0])
frutas.append("uva")
print("Ahora tengo", len(frutas), "frutas")''',
                    'expected_output': '''Mis frutas: ['manzana', 'banana', 'naranja']
Primera fruta: manzana
Ahora tengo 4 frutas''',
                    'validation_contains': ['[', ']', 'append', 'print'],
                    'hints': [
                        'Las listas van entre corchetes []',
                        'Los elementos se separan por comas',
                        'append() añade un elemento al final',
                        'len() te dice cuántos elementos hay'
                    ]
                },
                {
                    'title': 'Recorriendo listas',
                    'content': '''¡Excelente! Ahora aprenderás a recorrer listas.

Puedes usar `for` para procesar cada elemento de una lista:

• **for elemento in lista**: Recorre todos los elementos
• **for i in range(len(lista))**: Recorre por índices
• **enumerate()**: Te da posición y elemento

¡Es muy útil para procesar datos!''',
                    'code_example': '''colores = ["rojo", "verde", "azul"]
print("Mis colores favoritos:")
for color in colores:
    print("- Me gusta el", color)
    
print("\\nTotal de colores:", len(colores))''',
                    'expected_output': '''Mis colores favoritos:
- Me gusta el rojo
- Me gusta el verde
- Me gusta el azul

Total de colores: 3''',
                    'validation_contains': ['for', 'in', 'print'],
                    'hints': [
                        'for color in colores recorre cada elemento',
                        'La variable color toma el valor de cada elemento',
                        '\\n crea una línea nueva',
                        'Puedes usar cualquier nombre para la variable'
                    ]
                },
                {
                    'title': 'Creando funciones',
                    'content': '''¡Genial! Ahora aprenderás a crear tus propias funciones.

Las funciones son bloques de código reutilizable:

• **def**: Define una nueva función
• **Parámetros**: Información que recibe
• **return**: Valor que devuelve
• **Llamar**: Usar la función

¡Es como crear tus propias herramientas!''',
                    'code_example': '''def saludar(nombre):
    mensaje = "¡Hola, " + nombre + "!"
    return mensaje

# Usar la función
saludo = saludar("Ana")
print(saludo)
print(saludar("Luis"))''',
                    'expected_output': '''¡Hola, Ana!
¡Hola, Luis!''',
                    'validation_contains': ['def', 'return', 'print'],
                    'hints': [
                        'def nombre_funcion(parametros): define una función',
                        'Los parámetros van entre paréntesis',
                        'return devuelve un valor',
                        'Para usar la función, llámala con nombre_funcion()'
                    ]
                },
                {
                    'title': 'Funciones con múltiples parámetros',
                    'content': '''¡Muy bien! Ahora aprenderás funciones más avanzadas.

Las funciones pueden recibir varios parámetros y hacer cálculos:

• **Múltiples parámetros**: Separados por comas
• **Valores por defecto**: `parametro=valor`
• **Sin return**: La función solo ejecuta código
• **Con return**: Devuelve un resultado

¡Puedes crear funciones muy poderosas!''',
                    'code_example': '''def calcular_area(largo, ancho):
    area = largo * ancho
    return area

def presentar_resultado(largo, ancho, area):
    print(f"Un rectángulo de {largo}x{ancho} tiene área {area}")

# Usar las funciones
mi_area = calcular_area(5, 3)
presentar_resultado(5, 3, mi_area)''',
                    'expected_output': 'Un rectángulo de 5x3 tiene área 15',
                    'validation_contains': ['def', 'return', 'print'],
                    'hints': [
                        'Separa múltiples parámetros con comas',
                        'Puedes llamar una función desde otra',
                        'f"texto {variable}" es un f-string',
                        'Divide tareas complejas en funciones simples'
                    ]
                }
            ]
        },

        # Tutorial 4: Strings y texto
        {
            'id': 'strings_text',
            'title': 'Strings y texto',
            'description': 'Manipula cadenas de texto: concatenación, métodos y f-strings',
            'difficulty': 'Principiante',
            'sort_order': 2,
            'steps': [
                {
                    'title': 'Concatenar y medir texto',
                    'content': '''Las **cadenas** (strings) representan texto en Python.

• Se escriben entre comillas: `"Hola"` o `'Hola'`
• Puedes unirlas con `+`
• `len()` devuelve la cantidad de caracteres''',
                    'code_example': '''saludo = "Hola"
nombre = "Ana"
mensaje = saludo + ", " + nombre
print(mensaje)
print("Longitud:", len(mensaje))''',
                    'expected_output': '''Hola, Ana
Longitud: 9''',
                    'validation_contains': ['+', 'print'],
                    'hints': ['Usa + para unir strings', 'len() cuenta caracteres']
                },
                {
                    'title': 'Métodos de string',
                    'content': '''Los strings tienen métodos útiles:

• `.upper()` — mayúsculas
• `.lower()` — minúsculas
• `.strip()` — quita espacios al inicio y final
• `.replace(viejo, nuevo)` — sustituye texto''',
                    'code_example': '''texto = "  Python es genial  "
print(texto.strip().upper())
print(texto.replace("genial", "poderoso").strip())''',
                    'expected_output': '''PYTHON ES GENIAL
  Python es poderoso  ''',
                    'validation_contains': ['.upper', 'print'],
                    'hints': ['Llama al método con punto: texto.upper()', 'strip() elimina espacios extra']
                },
                {
                    'title': 'f-strings',
                    'content': '''Los **f-strings** insertan variables dentro del texto de forma legible:

• Escribe `f` antes de las comillas
• Usa `{variable}` dentro del texto
• Puedes poner expresiones: `{a + b}`''',
                    'code_example': '''producto = "manzanas"
cantidad = 5
precio = 1.5
total = cantidad * precio
print(f"Compré {cantidad} {producto} por {total} euros")''',
                    'expected_output': 'Compré 5 manzanas por 7.5 euros',
                    'validation_contains': ['f"', 'print'],
                    'hints': ['El prefijo f va antes de las comillas', 'Las variables van entre llaves {}']
                }
            ]
        },

        # Tutorial 5: Diccionarios
        {
            'id': 'dictionaries_basics',
            'title': 'Diccionarios',
            'description': 'Guarda datos con claves y valores usando diccionarios',
            'difficulty': 'Principiante',
            'sort_order': 3,
            'steps': [
                {
                    'title': 'Crear y acceder',
                    'content': '''Un **diccionario** asocia claves con valores:

• Se crea con llaves: `{"clave": valor}`
• Accedes con `diccionario["clave"]`
• Cada clave es única''',
                    'code_example': '''alumno = {"nombre": "Luis", "edad": 20, "curso": "Python"}
print(alumno["nombre"])
print("Edad:", alumno["edad"])''',
                    'expected_output': '''Luis
Edad: 20''',
                    'validation_contains': ['{', 'print'],
                    'hints': ['Usa llaves {} para el diccionario', 'Accede con corchetes y la clave']
                },
                {
                    'title': 'Modificar y añadir',
                    'content': '''Puedes cambiar valores o añadir nuevas claves:

• `d["clave"] = valor` — asigna o actualiza
• `del d["clave"]` — elimina una entrada
• `len(d)` — cuenta pares clave-valor''',
                    'code_example': '''inventario = {"manzanas": 10, "peras": 5}
inventario["manzanas"] = 12
inventario["uvas"] = 8
print(inventario)
print("Tipos de fruta:", len(inventario))''',
                    'expected_output': '''{'manzanas': 12, 'peras': 5, 'uvas': 8}
Tipos de fruta: 3''',
                    'validation_contains': ['=', 'print'],
                    'hints': ['Asigna con d["clave"] = valor', 'len() cuenta las claves']
                },
                {
                    'title': 'Recorrer diccionarios',
                    'content': '''Formas habituales de recorrer un diccionario:

• `.keys()` — todas las claves
• `.values()` — todos los valores
• `.items()` — pares (clave, valor)''',
                    'code_example': '''notas = {"matemáticas": 8, "historia": 7, "inglés": 9}
print("Asignaturas:")
for asignatura, nota in notas.items():
    print(f"  {asignatura}: {nota}")''',
                    'expected_output': '''Asignaturas:
  matemáticas: 8
  historia: 7
  inglés: 9''',
                    'validation_contains': ['for', '.items', 'print'],
                    'hints': ['items() devuelve pares clave-valor', 'for clave, valor in d.items()']
                }
            ]
        },

        # Tutorial 6: Tuplas y conjuntos
        {
            'id': 'tuples_sets',
            'title': 'Tuplas y conjuntos',
            'description': 'Colecciones inmutables (tuplas) y sin duplicados (sets)',
            'difficulty': 'Intermedio',
            'sort_order': 2,
            'steps': [
                {
                    'title': 'Tuplas inmutables',
                    'content': '''Las **tuplas** son como listas pero no se pueden modificar:

• Se escriben con paréntesis: `(1, 2, 3)`
• Útiles para coordenadas, registros fijos
• Se accede por índice como en listas''',
                    'code_example': '''punto = (10, 20)
print("X:", punto[0], "Y:", punto[1])
color_rgb = (255, 128, 0)
r, g, b = color_rgb
print(f"Rojo={r}, Verde={g}, Azul={b}")''',
                    'expected_output': '''X: 10 Y: 20
Rojo=255, Verde=128, Azul=0''',
                    'validation_contains': ['(', 'print'],
                    'hints': ['Las tuplas usan paréntesis', 'Puedes desempaquetar: a, b = tupla']
                },
                {
                    'title': 'Conjuntos (sets)',
                    'content': '''Un **set** guarda elementos únicos sin orden:

• `set([1, 2, 2, 3])` → `{1, 2, 3}`
• `.add()` añade un elemento
• Ideal para eliminar duplicados''',
                    'code_example': '''numeros = [1, 2, 2, 3, 3, 3, 4]
unicos = set(numeros)
print("Únicos:", unicos)
unicos.add(5)
print("Con 5:", unicos)''',
                    'expected_output': '''Únicos: {1, 2, 3, 4}
Con 5: {1, 2, 3, 4, 5}''',
                    'validation_contains': ['set', 'print'],
                    'hints': ['set() elimina duplicados', 'add() añade al conjunto']
                },
                {
                    'title': 'Operaciones entre conjuntos',
                    'content': '''Los sets permiten operaciones de teoría de conjuntos:

• `|` o `.union()` — unión
• `&` o `.intersection()` — intersección
• `-` o `.difference()` — diferencia''',
                    'code_example': '''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Unión:", a | b)
print("Comunes:", a & b)
print("Solo en A:", a - b)''',
                    'expected_output': '''Unión: {1, 2, 3, 4, 5, 6}
Comunes: {3, 4}
Solo en A: {1, 2}''',
                    'validation_contains': ['|', 'print'],
                    'hints': ['| une ambos conjuntos', '& devuelve elementos comunes']
                }
            ]
        },

        # Tutorial 7: Archivos
        {
            'id': 'file_handling',
            'title': 'Lectura y escritura de archivos',
            'description': 'Lee y escribe archivos de texto con open() y with',
            'difficulty': 'Intermedio',
            'sort_order': 3,
            'steps': [
                {
                    'title': 'Leer un archivo',
                    'content': '''Para leer archivos usas `open()`:

• `"r"` — modo lectura
• `.read()` — todo el contenido
• `.readlines()` — lista de líneas
• Siempre cierra con `.close()` o usa `with`''',
                    'code_example': '''# Simulación: en la práctica leerías un archivo real
contenido = "línea 1\\nlínea 2\\nlínea 3"
lineas = contenido.split("\\n")
for i, linea in enumerate(lineas, 1):
    print(f"Línea {i}: {linea}")''',
                    'expected_output': '''Línea 1: línea 1
Línea 2: línea 2
Línea 3: línea 3''',
                    'validation_contains': ['for', 'print'],
                    'hints': ['enumerate() da número y valor', 'split("\\n") separa por líneas']
                },
                {
                    'title': 'Escribir en un archivo',
                    'content': '''Para escribir archivos:

• `"w"` — sobrescribe (cuidado: borra el contenido anterior)
• `"a"` — añade al final
• `.write()` escribe texto
• `\\n` es salto de línea''',
                    'code_example': '''lineas = ["Primera línea", "Segunda línea", "Tercera línea"]
texto = "\\n".join(lineas)
print("Contenido a guardar:")
print(texto)
print(f"Total: {len(lineas)} líneas")''',
                    'expected_output': '''Contenido a guardar:
Primera línea
Segunda línea
Tercera línea
Total: 3 líneas''',
                    'validation_contains': ['join', 'print'],
                    'hints': ['join() une lista con separador', 'Modo "w" crea o sobrescribe']
                },
                {
                    'title': 'with — cierre automático',
                    'content': '''`with` abre el archivo y lo cierra automáticamente:

```python
with open("datos.txt", "r") as f:
    datos = f.read()
```

Es la forma recomendada en Python.''',
                    'code_example': '''# Patrón with (simulado sin archivo real)
datos = "nombre=Ana\\nedad=25"
with_context = True
if with_context:
    pares = {}
    for linea in datos.split("\\n"):
        clave, valor = linea.split("=")
        pares[clave] = valor
    print(pares)''',
                    'expected_output': "{'nombre': 'Ana', 'edad': '25'}",
                    'validation_contains': ['for', 'split', 'print'],
                    'hints': ['with garantiza que el archivo se cierre', 'split("=") separa clave y valor']
                }
            ]
        },

        # Tutorial 8: Errores y excepciones
        {
            'id': 'error_handling',
            'title': 'Manejo de errores',
            'description': 'Captura y gestiona errores con try, except y finally',
            'difficulty': 'Intermedio',
            'sort_order': 4,
            'steps': [
                {
                    'title': 'try y except',
                    'content': '''Cuando algo puede fallar, usa **try/except**:

• `try` — código que puede dar error
• `except` — qué hacer si falla
• Evita que el programa se cierre inesperadamente''',
                    'code_example': '''def dividir(a, b):
    try:
        resultado = a / b
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")

dividir(10, 2)
dividir(10, 0)''',
                    'expected_output': '''Resultado: 5.0
Error: no se puede dividir entre cero''',
                    'validation_contains': ['try', 'except', 'print'],
                    'hints': ['try envuelve el código arriesgado', 'except captura el tipo de error']
                },
                {
                    'title': 'Varios tipos de error',
                    'content': '''Puedes capturar errores específicos o varios:

• `except ValueError` — valor incorrecto
• `except (TypeError, ValueError)` — varios tipos
• `except Exception as e` — cualquier error con mensaje''',
                    'code_example': '''def convertir_entero(texto):
    try:
        numero = int(texto)
        print("Número válido:", numero)
    except ValueError:
        print(f"'{texto}' no es un entero")

convertir_entero("42")
convertir_entero("hola")''',
                    'expected_output': '''Número válido: 42
'hola' no es un entero''',
                    'validation_contains': ['try', 'ValueError', 'print'],
                    'hints': ['int() lanza ValueError si el texto no es número', 'Puedes usar f-string en el mensaje']
                },
                {
                    'title': 'else y finally',
                    'content': '''Bloques adicionales:

• `else` — se ejecuta si NO hubo error
• `finally` — siempre se ejecuta (limpieza, cerrar recursos)''',
                    'code_example': '''def procesar(valor):
    try:
        resultado = int(valor) * 2
    except ValueError:
        print("Entrada inválida")
    else:
        print("Éxito:", resultado)
    finally:
        print("Proceso terminado")

procesar("5")
print("---")
procesar("x")''',
                    'expected_output': '''Éxito: 10
Proceso terminado
---
Entrada inválida
Proceso terminado''',
                    'validation_contains': ['try', 'finally', 'print'],
                    'hints': ['else solo corre sin excepciones', 'finally siempre se ejecuta']
                }
            ]
        },

        # Tutorial 9: Módulos
        {
            'id': 'modules_packages',
            'title': 'Módulos e imports',
            'description': 'Organiza código en módulos y reutiliza librerías',
            'difficulty': 'Intermedio',
            'sort_order': 5,
            'steps': [
                {
                    'title': 'import básico',
                    'content': '''Python incluye muchos **módulos** listos para usar:

• `import math` — accedes con `math.sqrt()`
• `import random` — números aleatorios
• `import datetime` — fechas y horas''',
                    'code_example': '''import math
import random

print("Raíz de 16:", math.sqrt(16))
print("Número aleatorio:", random.randint(1, 10))
print("Pi:", round(math.pi, 2))''',
                    'expected_output': '''Raíz de 16: 4.0
Número aleatorio: 7
Pi: 3.14''',
                    'validation_contains': ['import', 'print'],
                    'hints': ['import carga un módulo completo', 'Usa modulo.funcion()']
                },
                {
                    'title': 'from ... import',
                    'content': '''Puedes importar solo lo que necesitas:

• `from math import sqrt, pi`
• `from random import choice`
• Evita `from modulo import *` (poco claro)''',
                    'code_example': '''from math import sqrt, pi
from random import choice

opciones = ["rojo", "verde", "azul"]
print("Color:", choice(opciones))
print("2 * pi =", round(2 * pi, 2))
print("sqrt(25) =", sqrt(25))''',
                    'expected_output': '''Color: verde
2 * pi = 6.28
sqrt(25) = 5.0''',
                    'validation_contains': ['from', 'import', 'print'],
                    'hints': ['from math import sqrt importa solo sqrt', 'choice() elige al azar de una lista']
                },
                {
                    'title': '__name__ == "__main__"',
                    'content': '''Patrón para scripts reutilizables:

• El código bajo `if __name__ == "__main__":` solo corre al ejecutar el archivo directamente
• Si importas el módulo, ese bloque no se ejecuta
• Muy usado en proyectos reales''',
                    'code_example': '''def saludar(nombre):
    return f"Hola, {nombre}!"

# Simulación del patrón __main__
ejecutar_directo = True
if ejecutar_directo:
    print(saludar("Python"))
    print("Script ejecutado como programa principal")''',
                    'expected_output': '''Hola, Python!
Script ejecutado como programa principal''',
                    'validation_contains': ['if', 'def', 'print'],
                    'hints': ['def define funciones reutilizables', 'El bloque if protege código de ejecución directa']
                }
            ]
        },

        # Tutorial 10: Comprensiones
        {
            'id': 'list_comprehensions',
            'title': 'Comprensiones de listas',
            'description': 'Crea listas y diccionarios de forma compacta y pythónica',
            'difficulty': 'Intermedio',
            'sort_order': 6,
            'steps': [
                {
                    'title': 'List comprehension básica',
                    'content': '''Sintaxis compacta para crear listas:

`[expresión for elemento in iterable]`

Equivalente a un bucle for pero en una línea.''',
                    'code_example': '''cuadrados = [x ** 2 for x in range(1, 6)]
print(cuadrados)
nombres = ["ana", "luis", "maría"]
mayusculas = [n.upper() for n in nombres]
print(mayusculas)''',
                    'expected_output': '''[1, 4, 9, 16, 25]
['ANA', 'LUIS', 'MARÍA']''',
                    'validation_contains': ['for', 'in', 'print'],
                    'hints': ['[x**2 for x in range(5)] crea cuadrados', 'Puedes llamar métodos como .upper()']
                },
                {
                    'title': 'Con condición',
                    'content': '''Añade un filtro con `if`:

`[expr for x in lista if condición]`

Solo incluye elementos que cumplan la condición.''',
                    'code_example': '''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print("Pares:", pares)
mayores = [n for n in numeros if n > 5]
print("Mayores que 5:", mayores)''',
                    'expected_output': '''Pares: [2, 4, 6, 8, 10]
Mayores que 5: [6, 7, 8, 9, 10]''',
                    'validation_contains': ['if', 'for', 'print'],
                    'hints': ['if va al final de la comprehension', '% 2 == 0 detecta números pares']
                },
                {
                    'title': 'Dict comprehension',
                    'content': '''Igual idea para diccionarios:

`{clave: valor for elemento in iterable}`

Muy útil para transformar datos.''',
                    'code_example': '''palabras = ["python", "es", "genial"]
longitudes = {p: len(p) for p in palabras}
print(longitudes)
doble = {n: n * 2 for n in range(1, 5)}
print(doble)''',
                    'expected_output': '''{'python': 6, 'es': 2, 'genial': 6}
{1: 2, 2: 4, 3: 6, 4: 8}''',
                    'validation_contains': ['for', '{', 'print'],
                    'hints': ['Usa llaves {} para dict comprehension', 'clave: valor for x in lista']
                }
            ]
        },

        # Tutorial 11: POO - Clases
        {
            'id': 'oop_intro',
            'title': 'Programación orientada a objetos',
            'description': 'Crea clases, objetos, atributos y métodos',
            'difficulty': 'Avanzado',
            'sort_order': 1,
            'steps': [
                {
                    'title': 'Definir una clase',
                    'content': '''Una **clase** es el molde de un objeto:

• `class Nombre:` define la clase
• Los objetos se crean llamando a la clase: `obj = Nombre()`
• Los atributos guardan datos del objeto''',
                    'code_example': '''class Perro:
    pass

mi_perro = Perro()
mi_perro.nombre = "Rocky"
mi_perro.edad = 3
print(mi_perro.nombre, "tiene", mi_perro.edad, "años")''',
                    'expected_output': 'Rocky tiene 3 años',
                    'validation_contains': ['class', 'print'],
                    'hints': ['class Nombre: define la clase', 'Asigna atributos con objeto.atributo = valor']
                },
                {
                    'title': '__init__ y self',
                    'content': '''`__init__` inicializa el objeto al crearlo:

• `self` referencia la instancia actual
• Los parámetros de `__init__` configuran el objeto
• Es el constructor de la clase''',
                    'code_example': '''class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"

p = Persona("Ana", 28)
print(p.presentarse())''',
                    'expected_output': 'Soy Ana y tengo 28 años',
                    'validation_contains': ['__init__', 'self', 'def'],
                    'hints': ['__init__ recibe self como primer parámetro', 'self.atributo guarda datos en el objeto']
                },
                {
                    'title': 'Métodos de instancia',
                    'content': '''Los **métodos** son funciones dentro de la clase:

• Siempre reciben `self` como primer argumento
• Pueden leer y modificar atributos
• Se llaman con `objeto.metodo()`''',
                    'code_example': '''class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Saldo: {self.saldo}"

c = Cuenta("Luis", 100)
print(c.depositar(50))
print(c.depositar(25))''',
                    'expected_output': '''Saldo: 150
Saldo: 175''',
                    'validation_contains': ['def', 'self', 'print'],
                    'hints': ['Los métodos modifican self.atributo', 'depositar es un método de instancia']
                }
            ]
        },

        # Tutorial 12: Herencia
        {
            'id': 'inheritance',
            'title': 'Herencia y polimorfismo',
            'description': 'Extiende clases y reutiliza comportamiento con herencia',
            'difficulty': 'Avanzado',
            'sort_order': 2,
            'steps': [
                {
                    'title': 'Clase hija',
                    'content': '''La **herencia** permite crear clases basadas en otras:

• `class Hijo(Padre):` hereda del padre
• La hija obtiene atributos y métodos del padre
• Puedes añadir o sobrescribir comportamiento''',
                    'code_example': '''class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"

g = Gato("Michi")
print(g.hablar())''',
                    'expected_output': 'Michi dice: Miau',
                    'validation_contains': ['class', 'def', 'print'],
                    'hints': ['class Gato(Animal) hereda de Animal', 'Sobrescribe hablar() en la subclase']
                },
                {
                    'title': 'super()',
                    'content': '''`super()` llama al método de la clase padre:

• Útil para extender, no solo reemplazar
• `super().__init__(...)` inicializa la parte del padre
• Evita duplicar código''',
                    'code_example': '''class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def info(self):
        return f"{self.marca}, {self.puertas} puertas"

c = Coche("Toyota", 4)
print(c.info())''',
                    'expected_output': 'Toyota, 4 puertas',
                    'validation_contains': ['super', '__init__', 'print'],
                    'hints': ['super().__init__() llama al constructor del padre', 'Añade atributos propios después']
                },
                {
                    'title': 'Polimorfismo',
                    'content': '''**Polimorfismo**: distintos objetos responden al mismo método de formas diferentes.

Muy útil cuando tratas varios tipos de forma uniforme.''',
                    'code_example': '''class Perro:
    def sonido(self):
        return "Guau"

class Gato:
    def sonido(self):
        return "Miau"

animales = [Perro(), Gato(), Perro()]
for a in animales:
    print(a.sonido())''',
                    'expected_output': '''Guau
Miau
Guau''',
                    'validation_contains': ['for', 'def', 'print'],
                    'hints': ['Cada clase implementa sonido() a su manera', 'El bucle trata todos igual']
                }
            ]
        },

        # Tutorial 13: Context managers
        {
            'id': 'context_managers',
            'title': 'Gestores de contexto',
            'description': 'Usa with y crea tus propios context managers',
            'difficulty': 'Avanzado',
            'sort_order': 3,
            'steps': [
                {
                    'title': 'with en la práctica',
                    'content': '''`with` garantiza limpieza automática de recursos:

• Archivos, conexiones, bloqueos
• Entra al bloque → ejecuta → sale siempre (incluso con error)
• Más seguro que open/close manual''',
                    'code_example': '''class Recurso:
    def __enter__(self):
        print("Recurso abierto")
        return self
    def __exit__(self, *args):
        print("Recurso cerrado")

with Recurso() as r:
    print("Trabajando con el recurso")''',
                    'expected_output': '''Recurso abierto
Trabajando con el recurso
Recurso cerrado''',
                    'validation_contains': ['with', '__enter__', 'print'],
                    'hints': ['__enter__ se ejecuta al entrar en with', '__exit__ se ejecuta al salir']
                },
                {
                    'title': 'contextlib.contextmanager',
                    'content': '''Con el decorador `@contextmanager` puedes crear gestores con yield:

• Código antes de `yield` → entrada
• Código después de `yield` → salida (limpieza)''',
                    'code_example': '''from contextlib import contextmanager

@contextmanager
def temporizador(nombre):
    print(f"Inicio: {nombre}")
    yield
    print(f"Fin: {nombre}")

with temporizador("tarea"):
    print("  Ejecutando...")''',
                    'expected_output': '''Inicio: tarea
  Ejecutando...
Fin: tarea''',
                    'validation_contains': ['@contextmanager', 'yield', 'with'],
                    'hints': ['@contextmanager convierte una función generadora', 'yield separa entrada y salida']
                }
            ]
        },

        # Tutorial 14: Generadores
        {
            'id': 'generators_iterators',
            'title': 'Generadores e iteradores',
            'description': 'Produce valores bajo demanda con yield y expresiones generadoras',
            'difficulty': 'Avanzado',
            'sort_order': 4,
            'steps': [
                {
                    'title': 'Función generadora',
                    'content': '''Una función con `yield` es un **generador**:

• No devuelve todo de golpe
• Produce un valor cada vez que se pide
• Ahorra memoria con secuencias grandes''',
                    'code_example': '''def contar_hasta(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for numero in contar_hasta(4):
    print(numero, end=" ")
print()''',
                    'expected_output': '1 2 3 4 ',
                    'validation_contains': ['yield', 'for', 'print'],
                    'hints': ['yield pausa la función y devuelve un valor', 'El bucle for consume el generador']
                },
                {
                    'title': 'next() e iteradores',
                    'content': '''Puedes avanzar manualmente con `next()`:

• `next(gen)` — siguiente valor
• `StopIteration` — cuando no quedan más
• Todo generador es un iterador''',
                    'code_example': '''def pares(limite):
    n = 0
    while n < limite:
        yield n
        n += 2

gen = pares(6)
print(next(gen), next(gen), next(gen))''',
                    'expected_output': '0 2 4',
                    'validation_contains': ['yield', 'next', 'print'],
                    'hints': ['next() pide el siguiente valor del generador', 'yield n produce cada par']
                },
                {
                    'title': 'Expresión generadora',
                    'content': '''Como list comprehension pero con paréntesis:

`(expr for x in iterable)` — generador lazy

No crea la lista completa en memoria.''',
                    'code_example': '''cuadrados = (x ** 2 for x in range(1, 6))
print("Primeros 3:", end=" ")
for i, c in enumerate(cuadrados):
    if i >= 3:
        break
    print(c, end=" ")
print()
print("Suma resto:", sum(cuadrados))''',
                    'expected_output': '''Primeros 3: 1 4 9 
Suma resto: 50''',
                    'validation_contains': ['for', 'sum', 'print'],
                    'hints': ['(x**2 for x in range(5)) es un generador', 'sum() consume los valores restantes']
                }
            ]
        },

        # Tutorial 15: Decoradores
        {
            'id': 'decorators_intro',
            'title': 'Decoradores',
            'description': 'Modifica funciones con decoradores y functools.wraps',
            'difficulty': 'Experto',
            'sort_order': 1,
            'steps': [
                {
                    'title': 'Funciones como objetos',
                    'content': '''En Python las funciones son objetos de primera clase:

• Puedes asignarlas a variables
• Pasarlas como argumento
• Devolverlas desde otra función''',
                    'code_example': '''def saludar(nombre):
    return f"Hola, {nombre}"

def ejecutar(func, valor):
    return func(valor)

resultado = ejecutar(saludar, "Python")
print(resultado)''',
                    'expected_output': 'Hola, Python',
                    'validation_contains': ['def', 'return', 'print'],
                    'hints': ['ejecutar recibe una función como parámetro', 'func(valor) la ejecuta']
                },
                {
                    'title': 'Decorador simple',
                    'content': '''Un **decorador** envuelve una función para añadir comportamiento:

• `@decorador` antes de `def`
• Equivalente a `func = decorador(func)`
• Muy usado para logging, permisos, caché''',
                    'code_example': '''def log_llamada(func):
    def envoltorio(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        return func(*args, **kwargs)
    return envoltorio

@log_llamada
def sumar(a, b):
    return a + b

print("Resultado:", sumar(3, 4))''',
                    'expected_output': '''Llamando a sumar
Resultado: 7''',
                    'validation_contains': ['@log_llamada', 'def', 'return'],
                    'hints': ['@log_llamada aplica el decorador', 'envoltorio llama a la función original']
                },
                {
                    'title': 'functools.wraps',
                    'content': '''`@wraps` preserva nombre y documentación de la función original:

```python
from functools import wraps
```

Es buena práctica en decoradores personalizados.''',
                    'code_example': '''from functools import wraps

def repetir(veces):
    def decorador(func):
        @wraps(func)
        def envoltorio(*args, **kwargs):
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return envoltorio
    return decorador

@repetir(2)
def decir(msg):
    print(msg)

decir("Hola")''',
                    'expected_output': '''Hola
Hola''',
                    'validation_contains': ['@wraps', '@repetir', 'print'],
                    'hints': ['@wraps(func) mantiene metadatos', 'Decoradores pueden recibir parámetros (veces)']
                }
            ]
        },

        # Tutorial 16: Async
        {
            'id': 'async_intro',
            'title': 'Programación asíncrona',
            'description': 'Introducción a async/await y asyncio',
            'difficulty': 'Experto',
            'sort_order': 2,
            'steps': [
                {
                    'title': 'async def y await',
                    'content': '''**async/await** permite concurrencia sin bloquear:

• `async def` define una corrutina
• `await` espera otra corrutina o tarea
• Ideal para I/O: red, archivos, APIs''',
                    'code_example': '''import asyncio

async def tarea(nombre, segundos):
    print(f"Inicio {nombre}")
    await asyncio.sleep(segundos)
    print(f"Fin {nombre}")
    return nombre

async def main():
    r = await tarea("A", 0.1)
    print("Completado:", r)

asyncio.run(main())''',
                    'expected_output': '''Inicio A
Fin A
Completado: A''',
                    'validation_contains': ['async', 'await', 'asyncio'],
                    'hints': ['async def crea una corrutina', 'await asyncio.sleep() simula espera sin bloquear']
                },
                {
                    'title': 'Ejecutar tareas en paralelo',
                    'content': '''`asyncio.gather()` ejecuta varias corrutinas a la vez:

• Más rápido que hacerlas una tras otra
• Todas deben ser async
• Recoge los resultados en una lista''',
                    'code_example': '''import asyncio

async def fetch(id):
    await asyncio.sleep(0.05)
    return f"datos-{id}"

async def main():
    resultados = await asyncio.gather(fetch(1), fetch(2), fetch(3))
    print(resultados)

asyncio.run(main())''',
                    'expected_output': "['datos-1', 'datos-2', 'datos-3']",
                    'validation_contains': ['asyncio.gather', 'await', 'print'],
                    'hints': ['gather ejecuta corrutinas concurrentemente', 'Devuelve lista de resultados']
                }
            ]
        },

        # Tutorial 17: Type hints y dataclasses
        {
            'id': 'typing_dataclasses',
            'title': 'Tipado y dataclasses',
            'description': 'Anotaciones de tipo, Optional y dataclasses',
            'difficulty': 'Experto',
            'sort_order': 3,
            'steps': [
                {
                    'title': 'Type hints',
                    'content': '''Las **anotaciones de tipo** documentan qué espera cada función:

• No obligan en tiempo de ejecución (por defecto)
• Ayudan a IDEs y herramientas como mypy
• `def f(x: int) -> str:`''',
                    'code_example': '''def area_rectangulo(largo: float, ancho: float) -> float:
    return largo * ancho

def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

print(area_rectangulo(5.0, 3.0))
print(saludar("Ana"))''',
                    'expected_output': '''15.0
Hola, Ana''',
                    'validation_contains': [':', '->', 'print'],
                    'hints': ['param: tipo anota el parámetro', '-> tipo anota el valor de retorno']
                },
                {
                    'title': 'Optional y listas tipadas',
                    'content': '''Del módulo `typing` (o sintaxis moderna Python 3.10+):

• `Optional[str]` — str o None
• `list[int]` — lista de enteros
• `dict[str, int]` — claves str, valores int''',
                    'code_example': '''from typing import Optional

def buscar(items: list[str], texto: str) -> Optional[int]:
    for i, item in enumerate(items):
        if item == texto:
            return i
    return None

frutas = ["manzana", "pera", "uva"]
print(buscar(frutas, "pera"))
print(buscar(frutas, "kiwi"))''',
                    'expected_output': '''1
None''',
                    'validation_contains': ['Optional', 'list', 'return'],
                    'hints': ['Optional[int] significa int o None', 'return None si no encuentra']
                },
                {
                    'title': '@dataclass',
                    'content': '''`@dataclass` genera automáticamente __init__, __repr__ y más:

```python
from dataclasses import dataclass
```

Ideal para estructuras de datos simples.''',
                    'code_example': '''from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0

p = Producto("Teclado", 49.99, 10)
print(p)
print(f"Total inventario: {p.precio * p.stock}")''',
                    'expected_output': '''Producto(nombre='Teclado', precio=49.99, stock=10)
Total inventario: 499.9''',
                    'validation_contains': ['@dataclass', 'class', 'print'],
                    'hints': ['@dataclass evita escribir __init__ manual', 'stock: int = 0 es valor por defecto']
                }
            ]
        },
    ]

# Función auxiliar para validación personalizada
def validate_tutorial_code(tutorial_id: str, step_index: int, code: str) -> dict:
    """
    Valida el código del paso usando validation_contains del paso actual.
    """
    tutorials_by_id = {t['id']: t for t in get_tutorials_config()}
    if tutorial_id not in tutorials_by_id:
        return {'valid': True, 'message': 'Código aceptado.'}

    tutorial = tutorials_by_id[tutorial_id]
    if step_index < 0 or step_index >= len(tutorial['steps']):
        return {'valid': True, 'message': 'Código aceptado.'}

    step = tutorial['steps'][step_index]
    required = step.get('validation_contains', [])
    if not required:
        return {'valid': True, 'message': '¡Buen trabajo! Continúa al siguiente paso.'}

    code_lower = code.lower()
    missing = [token for token in required if token.lower() not in code_lower]
    if missing:
        hints = step.get('hints', [])
        if hints:
            message = hints[0]
        else:
            message = f'Revisa tu código. Debería incluir: {", ".join(missing)}'
        return {'valid': False, 'message': message}

    return {'valid': True, 'message': '¡Buen trabajo! Continúa al siguiente paso.'}
