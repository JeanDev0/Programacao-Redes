print ("Digite -1 para parar")
lista_servidores = []
latencia = 0
while True:
 latencia = int(input("Qual a latência dos servidores (ms)? "))
 if latencia == -1:
  break
 lista_servidores.append(latencia)

print (lista_servidores)
menor = min(lista_servidores)

print (f"A menor latencia foi {menor}")