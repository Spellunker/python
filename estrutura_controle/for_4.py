#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print("Fim!")"""

# Função que vai jogar um dado entre 6 números
# For com range 1 a 7
# Se for impar continue
# Se o número for par e for sorteado pela função dado
# Imprimir a string "ACERTOU" e depois chamar o break
# Se não acertou chama o else... print("Não acertou o número!")

from random import randint

def dice_draw():
    return randint(1,6)

random_number = dice_draw()

for number in range (1, 7):
    if number % 2 != 0:
        continue
    elif number == random_number:
        print("Correct", number)
        break
else:
    print("You didn´t get the number")
