
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("10.209.1.40", 5000))

while True:
    mensagem = input("Digite uma mensagem: ")
    cliente.sendall(mensagem.encode())

    mesagemServidor = cliente.recv(1024)
    print(mesagemServidor.decode())