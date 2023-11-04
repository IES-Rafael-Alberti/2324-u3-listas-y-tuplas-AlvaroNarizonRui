"""Ejercicio 3.1.6¶
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista 
las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
asignaturas que el usuario tiene que repetir."""

def eliminar_asignaturas_aprobadas(asignaturas,notas):
    asignaturas_suspensas = []
    for i in range(len(asignaturas)):
        if notas[i] < 5:
            asignaturas_suspensas.append(asignaturas[i])
    return asignaturas_suspensas

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
    notas = []
    for i in range(len(asignaturas)):
        nota = int(input(f"Qué nota has sacado en {asignaturas[i]} : "))
        notas.append(nota)
    #Procesamiento
    asignaturas_suspensas = eliminar_asignaturas_aprobadas(asignaturas,notas)
    #Salida
    print(f"El usuario debe repetir : {asignaturas_suspensas}")
