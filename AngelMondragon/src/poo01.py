class Producto:
    """
        Clase producto. Propiedades de un producto.
    """
    def __init__(self, nombre: str, precio: float) -> None:
        """
            Inicializa un producto con nombre y precio.

            :param nombre: Nombre del producto.
            :param precio: Precio del producto.
        """
        self.nombre: str = nombre
        self.precio: float = precio

producto_uno = Producto("Pan integral", 30.00)
print(f"Producto: {producto_uno.nombre}, Precio: ${producto_uno.precio}")

# Property y setter
class ProductoSetter:
    """
        Clase producto. Propiedades de un producto.
    """
    def __init__(self, nombre: str, precio: float) -> None:
        """
            Inicializa un producto con nombre y precio.

            :param nombre: Nombre del producto.
            :param precio: Precio del producto.
        """
        self._nombre: str = nombre
        self._precio: float = precio
    
    @property
    def precio(self) -> float:
        """
            Getter Nos permite acceder a la propiedad de .precio pero sin pasarle los parentesis.
        """
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        """
            Nos permite modificar el valor de la propiedad .precio
        """
        self._precio = nuevo_precio

producto_dos = ProductoSetter("Leche deslactosada", 22.50)
print(f"Producto: {producto_dos._nombre}, Precio: ${producto_dos.precio}")