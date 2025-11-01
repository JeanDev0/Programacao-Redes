import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto("Mensagem".encode(),("10.209.1.40",5000))

data, _ = cliente.recvfrom(1024)
print (data.decode())