from src.unitarias_01 import Cliente, Producto

def test_validar_email_succes():
    #Arrange
    email_valido = "test@example.com"
    
    #Act
    cliente_test = Cliente("Test", email_valido)

    #Assert
    assert cliente_test.validar_email() is True

def test_validar_email_falla():
    #Arrange
    email_invalido = "testexample"

    #Act
    cliente_test = Cliente("Test", email_invalido)

    #Assert
    assert cliente_test.validar_email() is False

def test_validar_aplicacion_descuento_correcta():
    #Arrange
    precio = 100
    porcentaje_descuento = 10

    #Act
    producto_test = Producto(precio)

    #Assert
    assert producto_test.aplicar_descuento(porcentaje_descuento) == 90