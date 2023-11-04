import pytest

def test_loteria():
    numeros_ganadores = [2,4,3,6,5]
    numeros_ordenados = list(numeros_ganadores)
    numeros_ordenados.sort()
    assert numeros_ordenados == [2,3,4,5,6]

if __name__ == "__main__":
    pytest.main()