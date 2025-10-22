# args (Argumentos posicionales)
def procesar_datos(*args) -> None:
    '''
        Esta función procesa datos recibidos como argumentos posicionales.

        :param args: Argumentos posicionales que representan datos a procesar.
    '''
    print(f"Argumentos: {args}")

# kwargs (Argumentos con nombre)
def procesar_datos_kwargs(**kwargs) -> None:
    '''
        Esta función procesa datos recibidos como argumentos con nombre.

        :param kwargs: Argumentos con nombre que representan datos a procesar.
    '''
    print(f"Argumentos con nombre: {kwargs}")

procesar_datos(1, 2, 3, "Hola", True)
procesar_datos_kwargs(nombre="Angel", edad=30, activo=True)