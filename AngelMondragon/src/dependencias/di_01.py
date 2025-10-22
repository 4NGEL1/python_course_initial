class RespositorioBD:
    def __init__(self):
        pass

    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en la base de datos.")

class ServicePedido:
    def __init__(self, repositorio: RespositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido):
        print(f"Creando el pedido {pedido}.")
        self.repositorio.guardar(pedido)

repo = RespositorioBD()
service = ServicePedido(repo)
service.crear_pedido("Pedido #1234")