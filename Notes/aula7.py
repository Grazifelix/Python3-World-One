#Aula: Operadores Aritméticos
#16/12/20

# OPERADORES ARITMÉTICOS:(+) = Adição, (-) Subtração, (*) Multiplicação,
# (/)Divisão, (**) Exponenciação, (//)Divisão inteira, (%) Resto da divisão.

print('oi' + 'olá')#concatenando strings
print("="*20) #printa o simbolo de igual vinte vezes
pow(3,5)# É o mesmo que 3**5, só que 'pow()' é uma função interna do python.
8**(1/2)#Assim se calcula um raiz quadrada.
8**(1/3)# Assim se calcula uma raiz cubíca.

#OUTROS CONCEITOS
'''
nome = str(input('Digite seu nome:')) #por padrão o input é string, mas adicionaro 'str' deixa mais específico.
print('Seja bem vindo {:20}!'.format(nome))# Está escrevendo o nome em vinte espaços.
print('Seja bem vindo {:>20}!'.format(nome))# Faz o alinhamento do nome a direita.
print('Seja bem vindo {:<20}!'.format(nome))# Faz o alinhamento do nome a esquerda.
print('Seja bem vindo {:^20}!'.format(nome))# Faz o alinhamento do nome centralizado.
print('Seja bem vindo {:=^20}!'.format(nome))# Faz o alinhamento do nome centralizado, entre vinte caracteres iguais.
'''

#UTILIZANDO O FORMAT:
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro numero:"))
soma= n1+n2
mult = n1*n2
div=n1/n2
exp=n1**n2

print("O valor da soma é igual a {}, da multiplicação é igual a {}, divisão é igual a {} e exponenciação é igual a {}.".format(soma, mult, div, exp))
print("Divisão {:.4f}".format(div)) #esse ":.(numero)f" é um parametro que diz quantas casas decimais o numero vai ter.

print("Juntando ", end='')#passa um parametro para o print, onde o seu final não é uma quebra de linha. Voce pode adicionar qualquer coisa, por ex: end='>>>'.
print("prints.")

print("Este texto \n será quebrado \n ao meio.")#comando de quebra de linha.
