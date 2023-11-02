"""Ejercicio 3.1.1¶
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla."""

def listarAsignaturas(asignaturas):
    contenedor_asignaturas = ""
    for i in asignaturas:
        contenedor_asignaturas += i + "\n"
    return contenedor_asignaturas

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matematicas","Fisica","Química","Historia","Lengua"]
    #Procesamiento
    salida_asignaturas = listarAsignaturas(asignaturas)
    #Salida
    print(salida_asignaturas)