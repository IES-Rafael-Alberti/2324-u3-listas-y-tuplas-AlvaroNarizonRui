"""Ejercicio 3.1.11¶
Escribir un programa que almacene los vectores (1,2,3) 
y (-1,0,2) en dos listas y muestre por pantalla su producto 
escalar."""

def producto_escalar(vector_a,vector_b) -> list:
    sumatoria = 0
    for i in range(len(vector_a)):
        sumatoria += vector_a[i]*vector_b[i]
    return sumatoria

if __name__ == "__main__":
    #Entrada
    vector_a = [1,2,3]
    vector_b = [-1,0,2]
    #Procesamiento
    resultado_producto_escalar = producto_escalar(vector_a,vector_b)
    #Salida
    print(f"El producto escalar de los vectores {vector_a} y {vector_b} = {resultado_producto_escalar}")
