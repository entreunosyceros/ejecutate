import os, sys, subprocess, json, time

# Prueba de estrés: código con while True + input hasta 'fin'
CODE = r"""
contador = 0
suma = 0
while True:
    dato = input('Valor (fin para salir): ')
    if dato.strip().lower() == 'fin':
        break
    try:
        suma += int(dato)
        contador += 1
    except ValueError:
        print('ignorado', dato)
print('RESULT', contador, suma)
"""

# Generar inputs: 0..49 y luego fin
data_inputs = [str(i) for i in range(50)] + ['fin']

# Simular wrapper de precaptura (idéntico a enfoque en terminal)
wrapper = ["__ejecutate_inputs = iter(["] + ["    %s," % json.dumps(v) for v in data_inputs] + ["])\n"]
wrapper += [
    "def input(prompt=None):",
    "    try:",
    "        val = next(__ejecutate_inputs)",
    "    except StopIteration:",
    "        val = ''",
    "    if prompt: print(prompt, end='')",
    "    return val",
    ""
]
final_code = '\n'.join(wrapper) + CODE

start = time.time()
proc = subprocess.run([sys.executable, '-u', '-c', final_code], capture_output=True, text=True)
elapsed = time.time() - start

out = proc.stdout.strip().splitlines()
result_line = next((l for l in out if l.startswith('RESULT ')), None)
rc = proc.returncode

summary = {
    'returncode': rc,
    'elapsed_seconds': round(elapsed, 3),
    'result_line': result_line,
    'stdout_tail': out[-5:],
    'stderr': proc.stderr.strip()[:200]
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
