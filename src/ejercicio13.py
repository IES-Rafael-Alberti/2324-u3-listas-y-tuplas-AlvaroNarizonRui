"""
Ejercicio 3.1.13¶
Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por 
pantalla su media y desviación típica."""

def media_numeros(lista_numeros) -> int:
    sumatoria = 0
    for i in lista_numeros:
        sumatoria += int(i)
    media = sumatoria / len(lista_numeros)
    return media

if __name__ == "__main__":
    #Entrada
    numeros = input("Escribe una serie de números separados por comas : ")
    lista_numeros = numeros.split(",")
    #Procesamiento
    media = media_numeros(lista_numeros)
    #Salida
    print(f"Media : {media}")