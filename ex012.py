# dar 5% de desconto
# 18/02/21

price = float(input("Insira o valor do produto:"))
discount = price * 0.05
finalValue = price - discount

print("O desconto de 5% sobre o valor de {:.2f} é de: R$ {:.2f}".format(price, discount))
print("O valor final a ser pago é: R$ {:.2f}".format(finalValue))