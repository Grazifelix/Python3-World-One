#Atividade do antecessor e sucessor
#29/01/21

num = int(input("Digite um número:"))


def ant(a):
    a = a - 1
    return a


def suc(b):
    b = b + 1
    return b


while True:
    print("Numero informado: {}; \n Seu antecessor: {}; \n Seu sucessor: {}.".format(num, ant(num), suc(num)))
    break
