mac = input("Qual o endereço Mac? ")
mac = mac.upper()
mac = mac.replace(";",":")
if mac[:8]== "00:1A:2B":
 print ("Esse MAC é Intel")
else:
 print("Esse MAC é Asus")
