"""Ejercicio 3.1.12¶
Escribir un programa que almacene las matrices A=(123456) 
y B=(−100111) en una lista y muestre por pantalla su producto. 
Nota: Para representar matrices mediante listas usar listas 
anidadas, representando cada vector fila en una lista."""

def producto_matrices(matriz_a,matriz_b) -> list:
    matriz_c = [[0,0,0],[0,0,0]]
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_b)):
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_c
if __name__ == "__main__":
    #Entrada
    matriz_a = [[1,2,3],[4,5,6]]
    matriz_b = [[-1,0,0],[1,1,1]]
    #Procesamiento
    matriz_c = producto_matrices(matriz_a,matriz_b)
    #Salida
    print(f"{matriz_a} x {matriz_b} = {matriz_c}")