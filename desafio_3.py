print('a) Resposta: ', end='')
a = 1
for n in range (5):
    print(f'{a}..',end='')
    a += 2
print('\n')

print('b) Resposta: ', end='')
a = 2
for n in range (7):
    print(f'{a}..', end='')
    a += a
print('\n')

print('c) Resposta: ', end='')
n = 0
p = 0
while p < 8:
    n *= n
    print(f'{n}..', end='')
    p += 1
    n = p
print('\n')

print('d) Resposta: ', end='')
a = 2
for n in range (5):
    resultado = a ** 2
    print(f'{resultado}..', end='')
    a += 2
print('\n')

print('e) Resposta: ', end='')
a = 0
b = 1
print(f'{a}.. {b}.. ', end='')
for n in range(6):
    c = a + b
    print(f'{c}.. ', end='')
    a = b
    b = c
print('\n')

print(f'f) Resposta: 2..10..12..16..17..18..19..200') #A lógica desta questão dada a sequencia de números é que todos se iniciam com a letra D, sendo assim a próxima seria 200.

