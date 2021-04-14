#09/12/20

#1
n1 = input('Digite um valor:')
print(type(n1)) #Vai retornar o tipo da variavél. Nesse caso por defalt será string.

#2
print('VAMOS SOMAR!')
x = int(input("Escreva um numero para X:"))
y = int(input('Escreva outro numero para Y:'))
soma = x + y
print('A soma entre {0} e {1} é igual a {2}.'.format(x,y,soma))

#3
n = input('Digite um valor:')
print(n.isnumeric()) #metodo que retorna uma resposta boleana a pergunta, 'é numerico?'

n = input('Digite um valor:')
print(n.isalpha()) #retorna em valor boleano se a variavél é alfabetica(letra) ou nao.

n = input('Digite um valor:')
print(n.isalnum()) #retorna valor boleano para se a variavel é alfanumerica ou não.

n = input('Digite um valor:')
print(n.isupper()) #retorna valor boleano(true ou false) se todas as letras estiverem maisculas.

#EXISTEM MUITOS OUTROS TIPOS DE .IS() PARA TESTAR DIFERENTES SITUAÇÕES!