from src.ejercicio7 import recortar_abecedario_en_multiplos_de_3
import pytest
import string

def test_recortar_abecedario_en_multiplos_de_3():
    abecedario = list(string.ascii_lowercase)
    resultado_esperado = ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'o', 'q', 'r', 't', 'u', 'w', 'x', 'z']
    assert recortar_abecedario_en_multiplos_de_3(abecedario) == resultado_esperado

if __name__ == "__main__":
    pytest.main()