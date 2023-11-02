"""Ejercicio 3.1.5¶
Escribir un programa que almacene en una lista los números del 1 al 10 y 
los muestre por pantalla en orden inverso separados por comas."""

def lista_reversa(numeros):
    contenedor = ""
    for i in range(len(numeros)-1,0,-1):
        if i == 0:
            contenedor += str(numeros[i])
        else:
            contenedor += str(numeros[i]) + ","
    return contenedor
if __name__ == "__main__":
    #Entrada
    numeros = list(range(1,10+1,1))
    #Procesamiento
    lista_reversa = lista_reversa(numeros)
    #Salida
    print(f"Tus numeros : {numeros} \n Resultado: {lista_reversa}")

