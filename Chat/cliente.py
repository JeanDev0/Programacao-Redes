import customtkinter

customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk()
janela.geometry("800x500")
janela.title("Chat IFRN Redes")

label_nome = customtkinter.CTkLabel(janela, text="Digite seu nome")
label_nome.pack(pady=(10,5))

janela.mainloop()