import aula98_modulo
import importlib

for i in range(10):
    print(i)
    import aula98_modulo

    # singleton - só tem uma instância dele no programa inteiro

for i in range(10):
    importlib.reload(aula98_modulo)
