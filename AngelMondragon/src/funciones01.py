def saludar(nombre: str) -> str:
    '''
        Esta función devuelve un saludo.

        Parámetros:
            nombre (str): El nombre de la persona a saludar.
    '''
    return f"¡Hola {nombre}!"

print(saludar("Angel"))

def saludo_generico(nombre: str = "Usuario") -> str:
    '''
        Esta función devuelve un saludo genérico.

        Parámetros:
            nombre (str): El nombre de la persona a saludar. Por defecto es "Usuario".
    '''
    return f"¡Hola {nombre}!"

print(saludo_generico())

# Funcion con argumento kwargs

# Funcion lambda
def suma(num1: int, num2: int) -> int:
    '''
        Esta función devuelve la suma de dos números.
        Parámetros:
            num1 (int): El primer número.
            num2 (int): El segundo número.
    '''
    return num1 + num2

suma_lambda = lambda num1, num2: num1 + num2

print(suma(3, 5))
print(suma_lambda(4, 6))

# Map y filter con funciones lambda
list_numeros = [1, 2, 3, 4, 5]
set_numeros = {1, 2, 3, 4, 5, 3, 2}

cuadrado_de_numero = lambda x: x**2

tipo_dato = type(map(cuadrado_de_numero, list_numeros))
cuadrados = list(map(cuadrado_de_numero, list_numeros))

print("Numeros cuadrados:", cuadrados)
print("Tipo de dato de map:", tipo_dato)

tipo_dato = type(map(cuadrado_de_numero, set_numeros))
cuadrados = list(map(cuadrado_de_numero, set_numeros))

print("Numeros cuadrados:", cuadrados)
print("Tipo de dato de map:", tipo_dato)

# Filter
pares = list(filter(lambda x: x % 2 == 0, list_numeros))
print("Numeros pares:", pares)