v_media_carro = 0
v_media_caminhao = 0
distancia = 100
velcar = 110
velcami = 80
pcami = 0.17

t = (distancia / velcami) + pcami
v_media_caminhao = distancia / t

print(v_media_caminhao)