# Imprimir tabuada a partir de um numero
# 18/02/21

n = int(input("Insira um numero:"))

for i in range(1,10+1):
   mult = n * i
   print("{} x {} = {}\n".format(n, i, mult))
