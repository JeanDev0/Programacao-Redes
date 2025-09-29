import os   

path = "C:\\Users\\20242144030026\\Desktop\\ProgramacaoRedes\\Programacao-Redes\\Lista 1"

files = os.listdir(path)
contagem = []

for file in files:
    if file[-3:] == ".py":
        contagem.append(file) 

print (len(contagem))