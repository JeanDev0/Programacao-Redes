import threading
import time

def imprimir():
    for i in range(5):
        print(i)
        time.sleep(2)

tt = threading.Thread (target=imprimir,)
tt.start()

ttt = threading.Thread (target=imprimir,)
ttt.start()