import os
import random

def select_word():
    os.system("clear")
    word = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        f = f.readlines()
        for line in f:
            word.append(line.strip('\n'))
    maximo = len(word)
    sorteo = random.randint(0, maximo)
    palabra = word[sorteo]
    palabra = palabra.swapcase()
    return(palabra)


def ocultar_palabra(palabra):
    tamano_oculto = len(palabra)
    palabra_oculta = ""
    for i in palabra:
        palabra_oculta = palabra_oculta + "_"
    return(palabra_oculta)


def game(palabra):
    palabra_oculta = ocultar_palabra(palabra)
    adivinando = ""
    while palabra_oculta != palabra:
        # os.system("clear")
        print("Intenta adivinar la palabra oculta: ")
        print(palabra_oculta)
        letra = input("Ingresa una letra: ")
        letra = letra.capitalize()
        for i in palabra:
            if i == letra:
            #     adivinando = adivinando + letra
            # elif i != "_":
                 adivinando = adivinando + i
            else:
                adivinando = adivinando + "_"
        palabra_oculta = adivinando




def run():
    palabra = select_word()
    print(palabra)
    game(palabra)


if __name__ == '__main__':
    run()