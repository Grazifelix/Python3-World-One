# Imprimir tabuada a partir de um numero
# 18/02/21

n = int(input("Insira um numero:"))

print("-"*12)
for i in range(1,10+1):
   mult = n * i
   print("{} x {} = {}".format(n, i, mult))
print("-"*12)

'''
22/04/21
#Como ele fez:
print("-"*12)
print("{} x {:2} = {}".format(n, 1, n*1))
print("{} x {:2} = {}".format(n, 2, n*2))
print("{} x {:2} = {}".format(n, 3, n*3))
print("{} x {:2} = {}".format(n, 4, n*4))
print("{} x {:2} = {}".format(n, 5, n*5))
print("{} x {:2} = {}".format(n, 6, n*6))
print("{} x {:2} = {}".format(n, 7, n*7))
print("{} x {:2} = {}".format(n, 8, n*8))
print("{} x {:2} = {}".format(n, 9, n*9))
print("{} x {:2} = {}".format(n, 10, n*10))
print("-"*12)
'''