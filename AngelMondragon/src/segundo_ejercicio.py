def generar_fibonacci(*args, **kwargs):
    """
    Genera la serie de Fibonacci usando 'yield'.

    Puede ser controlado por:
    - *args: El primer argumento se interpreta como la cantidad de términos a generar.
    - **kwargs: El valor de la clave 'limite' se interpreta como el valor máximo del término.
    """
    a, b = 0, 1
    cantidad = 0
    limite = float('inf')

    if args:
        type_of_first_arg = type(args[0])
        if type_of_first_arg is int and args[0] >= 0:
            cantidad = args[0]
        else:
            print("Advertencia: El argumento de cantidad debe ser un entero no negativo.")
            return
    
    if 'limite' in kwargs and kwargs['limite'] is not None:
        try:
            limite = float(kwargs['limite'])
        except ValueError:
            print("Advertencia: El límite debe ser un valor numérico.")
            return
    contador = 0
    
    if (cantidad > 0 and contador < cantidad) or (a <= limite):
        yield a
        contador += 1

    if (cantidad > 1 and contador < cantidad) or (b <= limite):
        yield b
        contador += 1

    while True:
        a, b = b, a + b
        
        if (cantidad > 0 and contador >= cantidad):
            break
        
        if (b > limite):
            break
            
        yield b
        contador += 1


# Pruebas de la función generar_fibonacci

print("Usando *args Cantidad de términos")
N_Fibonacci: int = 10
fib_por_cantidad = generar_fibonacci(N_Fibonacci)
print(f"Fibonacci ({N_Fibonacci} términos): {list(fib_por_cantidad)}")

print("\nUsando **kwargs clave 'limite'")
fib_por_limite = generar_fibonacci(limite=50)
print("Fibonacci (hasta límite 50):")
for num in fib_por_limite:
    print(num, end=", ")
print()

print("\nUsando el Generador directamente (Iterador)")
generador = generar_fibonacci(N_Fibonacci)

for num in generador:
    print(num)