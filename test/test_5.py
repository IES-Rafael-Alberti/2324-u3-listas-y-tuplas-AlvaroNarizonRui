from src.ejercicio5 import lista_reversa
import pytest

def test_lista_reversa():
    numeros = list(range(1,10+1,1))
    resultado = lista_reversa(numeros)
    assert lista_reversa(numeros) == resultado

if __name__ == "__main__":
    pytest.main()