import customtkinter
from CTkMessagebox import CTkMessagebox

def conectar():
    global nome
    global cliente
    nome_valor = campo_nome.get().strip()
    if nome_valor is None or nome_valor == "":
        CTkMessagebox(title="Erro", message="Antes, Digite seu nome", icon="warning")
        return

customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk()
janela.geometry("1000,650")
janela.title("Chat IFRN Redes")

label_nome = customtkinter.CTkLabel(janela, text="Digite seu nome")
label_nome.pack(pady=(35,5))
campo_nome = customtkinter.CTkEntry(janela, width=250)
campo_nome.pack(pady=10)

botao_conectar = customtkinter.CTkButton(janela, text="Conectar", command=conectar)
botao_conectar.pack(pady=(0,10))

memo_mensagens = customtkinter.CTkTextbox(janela, width=760, height=300, state="disable")
memo_mensagens.pack(padx=10, pady=60, fill="both", expand=True)

frame = customtkinter.CTkFrame(janela)
frame.pack(fill="x", padx=10, pady=(0,10))

campo_mensagem = customtkinter.CTkEntry(frame, state="disable")
campo_mensagem.pack (side="left", fill="x", expand=True, padx=(0,10))

botao_enviar = customtkinter.CTkButton(frame, text="Enviar", command=None, state="disable")
botao_enviar.pack (side="right")

cliente = None
nome = None

janela.mainloop()