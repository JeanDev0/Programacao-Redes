import threading    
import time 

def imprimir_nome_thread(nome):
    while True:
        print (nome)
        time.sleep(2)
