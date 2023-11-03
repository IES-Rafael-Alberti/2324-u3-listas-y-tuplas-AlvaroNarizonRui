"""
Ejercicio 3.1.9¶
Escribir un programa que pida al usuario una palabra y 
muestre por pantalla el número de veces que contiene cada vocal.
"""
def cuenta_vocales(lista_palabra):
    lista_repeticiones = []
    for j in vocales:
        contador = 0
        for i in range(len(lista_palabra)):
            if j == lista_palabra[i]:
                contador += 1
        lista_repeticiones.append(contador)
    return lista_repeticiones
        

if __name__ == "__main__":
    #Entrada
    palabra = input("Escribe una palabra : ")
    lista_palabra = []
    for i in range(len(palabra)):
        lista_palabra.append(palabra[i])
    vocales = ["a","e","i","o","u"]
    #Procesamiento
    repeticiones = cuenta_vocales(lista_palabra)
    #Salida
    print(f"La palabra que introdujiste : {palabra} \n Las vocales que se repiten : \n {vocales[0]}={repeticiones[0]} \n {vocales[1]}={repeticiones[1]} \n {vocales[2]}={repeticiones[2]} \n {vocales[3]}={repeticiones[3]} \n {vocales[4]}={repeticiones[4]}")
    