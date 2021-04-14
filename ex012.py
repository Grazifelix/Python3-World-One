# dar 5% de desconto
# 18/02/21

price = float(input("Insira o valor do produto:"))
discount = price * 0.05
finalValue = price - discount

print("O desconto final de 5% sobre o valor de {:.2f} é: {:.2f} reais.".format(price, finalValue))
