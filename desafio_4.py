v_media_carro = 110
v_media_caminhao = 0
distancia = 100 #Ponto de referência adicionado em Ribeirão Preto
velcar = 110
velcami = 80
pedagio = 0.17 #Valor convertido em hora
t = 0

car = velcar * t #Representação do cálculo para equação horária do carro

cami = distancia - (velcami * t) #Representação para cálculo de equação horária do caminhão
t_sem_pedagio = distancia / 80 #Cálculo do percurso sem pedágio
t_com_pedagio = t_sem_pedagio + 0.17 #Cálculo do percurso com pedágio

v_media_caminhao = distancia / t_com_pedagio #Cálculo de velocidade média do caminhão

resposta = (velcar * distancia) / (v_media_carro + v_media_caminhao) #Calculo para definir o ponto em que cruzam (São exclusos os valores de tempo e igualar ambos carro e caminhão para encontrar o ponto em que se cruzam)
print(f'Esta é a distância em que os veículo se cruzam: {resposta:.2f}km, ambos estão a mesma distância de Ribeirão Preto.') # O calculo foi para representar em qual ponto os veículos cruzaram, porém em relação a estar mais próximo do ponto de referência (Ribeirão Preto) sempre será o mesmo, ambos estarão a uma mesma distância.