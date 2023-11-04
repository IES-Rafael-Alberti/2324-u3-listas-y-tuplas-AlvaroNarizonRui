"""Ejercicio 3.1.4¶
Escribir un programa que pregunte al usuario los números ganadores 
de la lotería primitiva, los almacene en una lista y 
los muestre por pantalla ordenados de menor a mayor."""

if __name__ == "__main__":
    #Entrada
    entrada_ganadores = input("Cuáles fueron los números ganadores de la lotería (X-X-X-X-X-X) : ")
    numeros_ganadores = entrada_ganadores.split("-")
    #Procesamiento
    ganadores_ordenados = numeros_ganadores.sort()
    #Salida
    print(f"Estos fueron los números ganadores de la lotería: {ganadores_ordenados}")


