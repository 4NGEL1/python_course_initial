from src.dependencias.di_01_container import Container

def test_container_resolve_service_pedido():
    # Arrange
    container = Container()
    container.register("repositorio", lambda: RepositorioBD())
    container.register("service_pedido", lambda: ServicePedido(container.resolve("repositorio")()))

    # Act
    service = container.resolve("service_pedido")()

    # Assert
    assert service is not None
    assert isinstance(service, ServicePedido)
    assert isinstance(service.repositorio, RepositorioBD)