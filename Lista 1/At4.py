import datetime

list_adress_ip = []

print ("Para sair do programa digite 'Fim'")

while True:

    adress_ip = input ("Digite um endereço ip: ")
    if adress_ip.lower() == "fim":
        break
    list_adress_ip.append (adress_ip)

print ("Segue abaixo a lista de endereços ip")

now = datetime.datetime.now()
formated_date = now.strftime("%d-%m-%Y -- %H-%M-%S")

file_ip = open(f"{formated_date}.txt","w")
for adress_ip in list_adress_ip:
    print (adress_ip)
    file_ip.write(f"{adress_ip}\n")
file_ip.close()