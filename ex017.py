# 20/05/21
# Faça um programa que leia o
# comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# MEU MODO:
from math import sqrt

co = float(input("Escreva o comprimento do cateto oposto: "))
ca = float(input("Escreva o comprimento do cateto adjascente: "))
hipotenusa = sqrt((co**2) + (ca**2))

print("O valor da hipotenusa é:", round(hipotenusa, 2))


'''
# MODO CURSO EM VIDEO:
from math import hypot
co = float(input("Escreva o comprimento do cateto oposto: "))
ca = float(input("Escreva o comprimento do cateto adjascente: "))
h = hypot(co, ca)
print("O valor da hipotenusa é:", h)
'''