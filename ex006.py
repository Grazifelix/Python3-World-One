#Dobro, triplo, raiz quadrada
#29/01/21 - terminada em:04/02/21

n = int(input('Digie um numero:'))
d = n*2
t = n*3
r = n**(1/2)

print("O dobro de {} é: {}".format(n, d),
      "\n O triplo de {} é: {}".format(n, t),
      "\n A raiz quadrada de {} é: {}".format(n, r))


#versão sem usar operadores lógicos
'''

def suc(a):
    a = a + 1
    return a


def dobro(a):
    for i in range(a):
        a = suc(a)
    return a


def triplo(a):
    for i in range(dobro(a)):
        a = suc(a)
    return a


while True:
    n = int(input("Digite um numero:"))
    print("O dobro de {} é: {}".format(n, dobro(n)))
    print("O triplo de {} é: {}".format(n, triplo(n)))

    break
'''