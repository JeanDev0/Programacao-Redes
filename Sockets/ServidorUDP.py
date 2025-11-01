import socket   

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind (("0.0.0.0", 5000))
print ("Servidor UDP esperando mensagens...")

while True:
    data, address = servidor.recvfrom(1024)
    print (data.decode())
    servidor.sendto("Recebido".encode(), address)