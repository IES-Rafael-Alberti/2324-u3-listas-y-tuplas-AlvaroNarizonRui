"""Ejercicio 3.1.10¶
Escribir un programa que almacene en una lista los siguientes
precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla 
el menor y el mayor de los precios."""

if __name__ == "__main__":
    #Entrada
    precios = [50,75,46,22,80,65,8]
    #Procesamiento
    minimo = min(precios)
    maximo = max(precios)
    #Salida
    print(f"El precio menor : {minimo} euros\nEl precio mayor : {maximo} euros")
