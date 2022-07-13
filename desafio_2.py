a = 0
b = 1
lista_fibonacci = [0,1] #Criando lista para consultar a variável apresentada na entrada
numero = int(input('Digite um número para saber se ele está na sequência de Fibonacci: ')) #Variável de entrada do usuário
for n in range(20): #Criando a sequência de Fibonacci 
    c = a + b
    a = b
    b = c
    lista_fibonacci.append(c) #Adicionando a lista

print('Sequência Fibonacci: ', lista_fibonacci)#Apresentando ao usuário os 22 primeiros números da sequência
if numero in lista_fibonacci: #Criando condição para a existência ou não do valor de entrada na lista
    print(f'O número {numero} pertence a sequência Fibonacci.')
else:
    print(f'O número {numero} não pertence a sequência Fibonacci.')