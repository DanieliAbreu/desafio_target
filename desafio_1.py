indice = 13
soma = 0 #Ao final do processo encontraremos o valor de soma
k = 8

while k < indice:
    k = k + 1 #Acrescentando condição a variável k para não gerar loop infinito
    soma += k #Somando a variável soma a variável k
print(f'O valor da variável soma é {soma}.')
