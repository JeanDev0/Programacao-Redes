
while True:

    dispositivos_conectados = int(input("Quantos dispositivos tem conectados no wifi: "))

    if dispositivos_conectados > 10:
        print ("Muitos dispositivos conectados!")
    else:
        print ("Quantidade suficiente de dispositivos!")