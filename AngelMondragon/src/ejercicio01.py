# Comentario en una linea

'''
    Para comentarios multilinea
'''

variable_numero = 3
variable_bool = False

print(type(variable_numero))

variable_numero = "Hola Mundo"

print(type(variable_numero))

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Comprension de listas
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(type(pares), pares)