"""Ejercicio 3.1.3¶
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en
una lista, pregunte al usuario la nota que ha sacado en 
cada asignatura, y después las muestre por pantalla con 
el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una
de las correspondientes notas introducidas por el usuario."""

def mostrar_asignaturas_notas(asignaturas,notas):
    contenedor = ""
    for i in range(len(asignaturas)):
        contenedor += f"En {asignaturas[i]} has sacado {notas[i]}\n"
    return contenedor

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = []
    for i in range(len(asignaturas)):
        nota = int(input(f"Qué nota has sacado en {asignaturas[i]} : "))
        notas.append(nota)
    #Procesamiento
    salida_asignaturas_notas = mostrar_asignaturas_notas(asignaturas,notas)
    #Salida
    print(salida_asignaturas_notas)
