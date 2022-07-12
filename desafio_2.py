a = 0
b = 1
lista_fibonacci = [0,1]
numero = int(input('Digite um número para saber se ele está na sequência de Fibonacci: '))
for n in range(20):
    c = a + b
    a = b
    b = c
    lista_fibonacci.append(c)

print('Sequência Fibonacci: ', lista_fibonacci)
if numero in lista_fibonacci:
    print(f'O número {numero} pertence a sequência Fibonacci.')
else:
    print(f'O número {numero} não pertence a sequência Fibonacci.')