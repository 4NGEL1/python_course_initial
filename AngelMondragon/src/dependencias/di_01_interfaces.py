from abc import ABC, abstractmethod

class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en la base de datos.")

class RepositorioMongoDB(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en MongoDB.")

class ServicePedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido):
        print(f"Creando el pedido {pedido}.")
        self.repositorio.guardar(pedido)

repoBD: IRepositorioBD = RepositorioBD()
repoMongo: IRepositorioBD = RepositorioMongoDB()
service = ServicePedido(repoMongo)

service.crear_pedido("Pedido #1234")