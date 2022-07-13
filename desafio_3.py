print('a) Resposta: ', end='')
a = 1
for n in range (5): #Criando laço para apresentar os 5 primeiros valores
    print(f'{a}..',end='')
    a += 2 #Acrescentando condição a variável para não gerar loop infinito
print('\n')

print('b) Resposta: ', end='') 
a = 2
for n in range (7): #Criando laço para apresentar os 7 primeiros valores
    print(f'{a}..', end='')
    a += a #Acrescentando condição a variável para não gerar loop infinito
print('\n')

print('c) Resposta: ', end='')
n = 0
p = 0
while p < 8: #Criando laço para apresentar os 8 valores da sequência  
    n *= n
    print(f'{n}..', end='')
    p += 1 #Acrescentando condição a variável para não gerar loop infinito
    n = p #Igualando o valor para cálculo na próxima sequência do laço
print('\n')

print('d) Resposta: ', end='')
a = 2
for n in range (5): #Criando laço para apresentar os 5 primeiros valores
    resultado = a ** 2 
    print(f'{resultado}..', end='')
    a += 2 #Acrescentando a variável a, para não gerar loop infinito 
print('\n')

print('e) Resposta: ', end='')
a = 0
b = 1
print(f'{a}.. {b}.. ', end='') #Criando Sequência de Fibonacci
for n in range(6): #Criando laço para os 6 primeiros valores
    c = a + b
    print(f'{c}.. ', end='')
    a = b
    b = c
print('\n')

print(f'f) Resposta: 2..10..12..16..17..18..19..200') #A lógica desta questão dada a sequencia de números é que todos se iniciam com a letra D, sendo assim a próxima seria 200.

