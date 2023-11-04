from src.ejercicio8 import es_palindromo
import pytest

def test_es_palindromo_False():
    palabra = "pepe"
    lista_palabra = []
    for i in range(len(palabra)):
        lista_palabra.append(palabra[i])
    assert es_palindromo(lista_palabra) == False

def test_es_palindromo_True():
    palabra = "joj"
    lista_palabra = []
    for i in range(len(palabra)):
        lista_palabra.append(palabra[i])
    assert es_palindromo(lista_palabra) == True

if  __name__ == "__main__":
    pytest.main()