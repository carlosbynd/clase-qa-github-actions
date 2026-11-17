"""Reglas de negocio sencillas para una plataforma de venta de entradas.

Las cantidades se expresan en céntimos para evitar errores de redondeo.
"""

PRECIO_ENTRADA_CENTIMOS = 2500
DESCUENTO_MENOR_PORCENTAJE = 20


def calcular_total_centimos(cantidad: int, es_menor: bool = False) -> int:
    """Devuelve el precio total aplicando, si procede, descuento del 20 %."""
    if type(cantidad) is not int:
        raise TypeError("La cantidad debe ser un número entero")
    if cantidad < 1:
        raise ValueError("Debes reservar al menos una entrada")
    if cantidad > 8:
        raise ValueError("Máximo ocho entradas por reserva")

    importe = cantidad * PRECIO_ENTRADA_CENTIMOS
    if es_menor:
        importe = importe * 80 // 100  # 20 % de descuento (paga el 80 %)
    return importe
