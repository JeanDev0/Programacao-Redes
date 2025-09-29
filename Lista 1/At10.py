import os   

path = "C:\\Users\\20242144030026\\Documents\\ProgramacaoRedes\\"
folder_name = input("Digite o nome da pasta: ")

os.makedirs(f"{path} {folder_name}")
