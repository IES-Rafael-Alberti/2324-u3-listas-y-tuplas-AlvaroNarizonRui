"""
Ejercicio 3.1.8¶
Escribir un programa que pida al usuario una palabra y muestre por pantalla 
si es un palíndromo.
"""
def es_palindromo(lista_palabra:list) -> bool:
    palabra_al_reves = []
    for i in reversed(lista_palabra):
        palabra_al_reves.append(i)
    print(lista_palabra)
    print(palabra_al_reves)
    if palabra_al_reves == lista_palabra:
        return True
    else:
        return False

    
if __name__ == "__main__":
    #Entrada
    palabra = input("Escribe una palabra : ")
    lista_palabra = []
    for i in range(len(palabra)):
        lista_palabra.append(palabra[i])
    #Procesamiento
    es_palindromo = es_palindromo(lista_palabra)
    if es_palindromo == True:
        print(f"La palabra {palabra} es un palíndromo")
    else:
        print(f"La palabra {palabra} NO es un palíndromo")
