from src.ejercicio1 import listarAsignaturas
import pytest

def testAsignaturas():
    asignaturas = ["Matematicas","Fisica","Química","Historia","Lengua"]
    resultado = "Matematicas" + "\n" + "Fisica" + "\n" + "Química" + "\n" + "Historia" + "\n" + "Lengua" + "\n"
    assert listarAsignaturas(asignaturas) == resultado

if __name__ == "__main__":
    pytest.main()