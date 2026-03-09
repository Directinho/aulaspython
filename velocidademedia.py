
print("🏃Simulador de velocidade média🏃")
distancia = float(input("💨Informe a distância percorrida:"))
tempo = float(input("⏰Informe o tempo da Viagem(em Horas):"))

velocidade_media = distancia / tempo

print("🚨RESULTADO:🚨")
print("🚗A velocidade média é de {:.2f} km/h".format(velocidade_media))
print("💨Velocidade escolhida: {} km".format(distancia))
print("⏰Tempo escolhido: {} horas".format(tempo))