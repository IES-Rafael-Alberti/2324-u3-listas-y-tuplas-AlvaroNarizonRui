"""Ejercicio 3.1.2¶
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
sobre cada una de las asignaturas de la lista."""

def mostrar_asignaturas(asignaturas):
    mensaje = ""
    for asignatura in asignaturas:
        mensaje += f"Yo estudio {asignatura}\n"
    return mensaje

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matematicas","Fisica","Química","Historia","Lengua"]
    #Procesamiento
    salida_asignaturas = mostrar_asignaturas(asignaturas)
    #Salida
    print(salida_asignaturas)