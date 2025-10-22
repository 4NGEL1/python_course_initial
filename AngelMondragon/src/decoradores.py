import time

def decorador(func):
    def envoltura(*args):
        print("Antes de llamar a la función.")
        func(*args)
        print("Después de llamar a la función.")
    return envoltura

# Generar decorador que calcule el tiempo de ejecucion de una funcion

def decorador_tiempo_calc(func):
    def wrapper(*args):
        inicio = time.time()
        func(*args)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos.")
    return wrapper

@decorador
@decorador_tiempo_calc
def saludo(name: str = "Usuario"):
    # print("Inicio")
    print(f"¡Hola {name}! Bienvenido al curso de Python.")
    time.sleep(3)
    # print("Fin")


saludo("Juan")


