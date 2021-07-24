# 23/04/21

day = int(input("Por quantos dias o veículo foi utilizado? "))
km = float(input("Quantos quilometros foi percorrido? "))

result = (60*day) + (0.15*km)
print("O valor final a ser pago é: R$ {:.2f}".format(result))
