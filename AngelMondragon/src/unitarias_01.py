class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    
    def validar_email(self) -> bool:
        """
            Valida si el correo electrónico tiene un formato básico correcto.
            Retorna True si es válido, False en caso contrario.
        """
        if "@" in self.correo and "." in self.correo:
            return True
        return False
    
class Producto:
    def __init__(self, precio: float):
        self.precio = precio
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """
            Aplica un descuento al precio del producto.
            Retorna el precio con el descuento aplicado.
        """
        descuento = self.precio * (porcentaje / 100)
        return self.precio - descuento
    
client = Cliente("Angel", "angel@example.com")

print(client.validar_email())