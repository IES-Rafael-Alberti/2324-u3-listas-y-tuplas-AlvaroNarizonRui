from src.ejercicio13 import media_numeros
import pytest

def test_media():
    lista_numeros = [1,2,3,4,5]
    assert media_numeros(lista_numeros) == 3.0

if __name__ == "__main__":
    pytest.main()