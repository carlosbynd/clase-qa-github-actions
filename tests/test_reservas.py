"""Pruebas automatizadas de reglas de venta de entradas con pytest."""
import pytest
from reservas import calcular_total_centimos


def test_una_entrada_sin_descuento():
    assert calcular_total_centimos(1) == 2500


def test_tres_entradas_sin_descuento():
    assert calcular_total_centimos(3) == 7500


def test_dos_entradas_con_descuento_menor():
    assert calcular_total_centimos(2, es_menor=True) == 4000


def test_tres_entradas_con_descuento_menor():
    assert calcular_total_centimos(3, es_menor=True) == 6000


def test_cantidad_cero_no_es_valida():
    with pytest.raises(ValueError, match="al menos una"):
        calcular_total_centimos(0)


def test_cantidad_negativa_no_es_valida():
    with pytest.raises(ValueError):
        calcular_total_centimos(-2)


def test_no_pueden_reservarse_mas_de_ocho_entradas():
    with pytest.raises(ValueError, match="Máximo ocho"):
        calcular_total_centimos(9)


def test_cantidad_debe_ser_entero():
    with pytest.raises(TypeError):
        calcular_total_centimos("2")

