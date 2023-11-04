from src.ejercicio3 import mostrar_asignaturas_notas
import pytest

def test_asignaturas_notas():
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = [4,5,8,10,6]
    resultado = "En Matemáticas has sacado 4\nEn Física has sacado 5\nEn Química has sacado 8\nEn Historia has sacado 10\nEn Lengua has sacado 6\n"
    assert mostrar_asignaturas_notas(asignaturas,notas) == resultado

if __name__ == "__main__":
    pytest.main()