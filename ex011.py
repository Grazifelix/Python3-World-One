# Quanto de tinta usar?
# 18/02/21

a, b = list(map(float, input("Digite os numeros em metro da area:").split()))
area = a*b
tinta = area/2

print("A quantidade de tinta nescessária para pintar {} metros quadrados de area é: {} litros.".format(area, tinta))

#como ele fez
'''
larg = float(input("Digite a largura: "))
alt = float(input("Digite a altura: "))
area = a*b
tinta = area/2
print("A quantidade de tinta nescessária para pintar {} metros quadrados de area é: {} litros.".format(area, tinta))

'''