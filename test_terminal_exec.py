import os, sys, textwrap, subprocess, json, tempfile

# Este script prueba la lógica de precaptura usando EJECUTATE_TEST_INPUTS

CASES = [
    ("sin_input", "print('hola')" , []),
    ("un_input", "nombre = input('Nombre: '); print('Hola', nombre)", ["Ana"]),
    ("varios_inputs", textwrap.dedent('''\
        a = input('A: ')
        b = input('B: ')
        print('Suma', int(a)+int(b))
    '''), ["2","5"]),
]

def run_case(name, code, inputs):
    env = os.environ.copy()
    if inputs:
        env['EJECUTATE_TEST_INPUTS'] = json.dumps(inputs)
    # Ejecutar el código usando python -c con wrapper similar al terminal (simplificado)
    wrapper_lines = ["__ejecutate_inputs = iter(["] + [f"    {json.dumps(v)}," for v in inputs] + ["])"]
    wrapper_lines += ["def input(prompt=None):\n    try:\n        val = next(__ejecutate_inputs)\n    except StopIteration:\n        val = ''\n    if prompt: print(prompt, end='')\n    return val\n"]
    final_code = '\n'.join(wrapper_lines) + '\n' + code
    proc = subprocess.run([sys.executable,'-u','-c', final_code], capture_output=True, text=True, env=env)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def main():
    results = []
    for name, code, inputs in CASES:
        rc, out, err = run_case(name, code, inputs)
        results.append({"case": name, "rc": rc, "stdout": out, "stderr": err})
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
