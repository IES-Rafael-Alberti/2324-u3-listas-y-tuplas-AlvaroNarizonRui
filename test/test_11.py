from src.ejercicio11 import producto_escalar
import pytest

def test_producto_escalar():
    vector_a = [1,2,3]
    vector_b = [-1,0,2]
    assert producto_escalar(vector_a,vector_b) == 5

if __name__ == "__main__":
    pytest.main()