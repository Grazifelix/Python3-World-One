# 20/05/21
# Faça um programa que leia o
# comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

co = int(input("Escreva o comprimento do cateto oposto: "))
ca = int(input("Escreva o comprimento do cateto adjascente: "))
hipotenusa = sqrt((co**2) + (ca**2))

print("O valor da hipotenusa é:", hipotenusa)
