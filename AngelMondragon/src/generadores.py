# yield
def conteo_to_limit(lmit: int):
    """
        Cuenta desde 0 hasta el límite especificado.
        :param lmit: Límite hasta donde contar (exclusivo).
    """
    print("Inicio de funcion tradicional")
    for i in range(lmit):
        print("En la posicion", i)
    print("Fin de la funcion tradicional")

def conteo_to_limit_gen(lmit: int):
    """
        Cuenta desde 0 hasta el límite especificado, usando yield para generar los números uno a uno.
        :param lmit: Límite hasta donde contar (exclusivo).
    """
    print("Inicio de funcion con yield")
    for i in range(lmit):
        print("En la posicion", i)
        yield i
    print("Fin de la funcion con yield")

# conteo_to_limit(10)
for num in conteo_to_limit_gen(10):
    print("Numero generado:", num)