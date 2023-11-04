from src.ejercicio12 import producto_matrices
import pytest

def test_producto_matrices():
    matriz_a = [[1,2,3],[4,5,6]]
    matriz_b = [[-1,0,0],[1,1,1]]
    assert producto_matrices(matriz_a,matriz_b) == [[1,2,2],[1,5,5]]

if __name__ == "__main__":
    pytest.main()