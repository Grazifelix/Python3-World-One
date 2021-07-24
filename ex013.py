# Dar 15% de aumento
#19/02/21

wage = float(input("Insira o valor do seu salário:"))
aumento = wage * 0.15
finalValue = wage + aumento

print("15% de aumento é: R$ {:.2f}.".format(aumento))
print("Valor final do salário: R$ {:.2f}.".format(finalValue))