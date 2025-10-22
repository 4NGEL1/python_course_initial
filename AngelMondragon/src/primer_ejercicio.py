# Simular el cálculo del precio final de un producto con IVA aplicado
# Como lo haría un módulo de negocio en un sistema de punto de venta o e-commerce.

TASA_IVA: int = 16 

def calcular_precio_final(precio_base: float) -> float:
    """
    Calcula el precio final de un producto aplicando la tasa de IVA.

    :param precio_base: El precio del producto antes de impuestos.
    :return: El precio total (base + IVA).
    """
    monto_iva: float = precio_base * TASA_IVA / 100

    precio_final: float = precio_base + monto_iva

    return precio_final


# Pruebas
precio_producto_1: float = 100.00
precio_final_1: float = calcular_precio_final(precio_producto_1)

precio_producto_2: float = 499.99
precio_final_2: float = calcular_precio_final(precio_producto_2)

# Resultados
print("--- Simulación de Módulo de Negocio (Punto de Venta) ---")
print(f"Tasa de IVA aplicada: {TASA_IVA}%")

print("Producto 1:")
print(f"\tPrecio Base: ${precio_producto_1}")
print(f"\tPrecio Final: ${precio_final_1}")

print("Producto 2:")
print(f"\tPrecio Base: ${precio_producto_2}")
print(f"\tPrecio Final: ${precio_final_2}")