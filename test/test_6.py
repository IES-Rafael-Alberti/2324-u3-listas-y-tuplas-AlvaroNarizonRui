from src.ejercicio6 import eliminar_asignaturas_aprobadas
import pytest

def test_asignaturas_suspensas():
    asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
    notas = [5,4,4,5,10]
    assert eliminar_asignaturas_aprobadas(asignaturas,notas) == ["Fisica","Quimica"]

if __name__ == "__main__":
    pytest.main()