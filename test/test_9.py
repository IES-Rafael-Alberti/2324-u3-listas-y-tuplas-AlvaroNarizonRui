from src.ejercicio9 import cuenta_vocales
import pytest

def test_cuenta_vocales():
    palabra = "jorge"
    lista_palabra = []
    for i in range(len(palabra)):
        lista_palabra.append(palabra[i])
    assert cuenta_vocales(lista_palabra) == [0,1,0,1,0]

