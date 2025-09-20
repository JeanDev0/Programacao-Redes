
while True:

    velocidade = int(input("Qual a velocidade de download da sua net: "))

    if velocidade <= 10:
        print ("Conexão lenta!")
    elif velocidade <= 100:
        print ("Conexão normal!")
    else:
        print ("Conexão rápida")