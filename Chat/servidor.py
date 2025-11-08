import socket
import threading

clientes = []

def iniciar_servidor ():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 5000))
    servidor.listen()
    thread = threading.Thread(target=tratar_mensagens, args=(cliente,endereco))
    thread.start()

    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)

def tratar_mensagens(cliente,endereco):
    while True:
        try:
            mensagem = cliente.recv(100000)
            if mensagem:
                enviar_mensagem_cliente(mensagem, cliente)
        except Exception as e:
            print("Erro na recepção da mensagem", e)

def enviar_mensagem_cliente(mensagem, cliente_origem):
    for cliente in clientes:
        try:
            if cliente != cliente_origem:
                cliente.send(mensagem)
        except Exception as e:
            print("Erro na recepção da mensagem", e)

iniciar_servidor