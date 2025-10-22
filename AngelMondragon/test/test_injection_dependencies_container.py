from src.dependencias.di_01_container import Container, RepositorioBD, ServicePedido
from unittest.mock import Mock

def test_container_resolve_service_pedido():
    # Arrange
    container = Container()
    container.register("repositorio", lambda: RepositorioBD())
    container.register("service_pedido_2", lambda: ServicePedido(container.resolve("repositorio")()))

    # Act
    service = container.resolve("service_pedido_2")()

    # Assert
    assert service is not None
    assert isinstance(service, ServicePedido)
    assert isinstance(service.repositorio, RepositorioBD)

def test_service_pedido_crear_pedido_calls_guardar():
    # Arrange
    mock_repositorio = Mock(spec=RepositorioBD)
    service = ServicePedido(mock_repositorio)
    pedido = "Pedido #5678"
    # Act
    service.crear_pedido(pedido)
    # Assert
    mock_repositorio.guardar.assert_called_once_with(pedido)

def test_container_resolve_invalid_service():
    # Arrange
    container = Container()
    # Act & Assert
    try:
        container.resolve("invalid_service")
        assert False, "Expected ValueError for invalid service resolution"
    except ValueError as e:
        assert str(e) == "Service 'invalid_service' not found in container."

def test_service_pedido_with_different_repositorio():
    # Arrange
    class OtroRepositorio(RepositorioBD):
        def guardar(self, pedido):
            print(f"Guardando el pedido {pedido} en otro repositorio.")

    otro_repositorio = OtroRepositorio()
    service = ServicePedido(otro_repositorio)
    pedido = "Pedido #91011"
    # Act
    service.crear_pedido(pedido)
    # Assert
    assert service.repositorio is otro_repositorio