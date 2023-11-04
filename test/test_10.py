import pytest

def test_maximo():
    precios = [50,75,46,22,80,65,8]
    assert max(precios) == 80

def test_minimo():
    precios = [50,75,46,22,80,65,8]
    assert min(precios) == 8

    if __name__ == "__main__":
        pytest.main()