import string
"""
Ejercicio 3.1.7¶
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""
def recortar_abecedario_en_multiplos_de_3(abecedario:list) -> list:
    abecedario_recortado = []
    for i in range(len(abecedario)):
        if i % 3 != 0:
            abecedario_recortado.append(abecedario[i])
    return abecedario_recortado


if __name__ == "__main__":
    #Entrada
    abecedario = list(string.ascii_lowercase)
    #Procesamiento
    abecedario_recortado = recortar_abecedario_en_multiplos_de_3(abecedario)
    #Salida
    print(f"El abecedario inicial : {abecedario} \n Sin las posiciones multiplos de 3: {abecedario_recortado}")