from src.ejercicio2 import mostrar_asignaturas
import pytest

def test_mostrar_asignaturas():
    asignaturas = ["Matematicas","Fisica","Química","Historia","Lengua"]
    resultado = "Yo estudio Matematicas\nYo estudio Fisica\nYo estudio Química\nYo estudio Historia\nYo estudio Lengua\n"
    assert mostrar_asignaturas(asignaturas) == resultado

if __name__ == "__main__":
    pytest.main()
