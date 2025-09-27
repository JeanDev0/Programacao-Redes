commum_port = [80, 443, 22, 21]
port = int(input ("Digite o número da porta: "))

if port in commum_port:
    print (f"A porta {port} é comum.")
else:
    print ("Não é uma porta comum.")