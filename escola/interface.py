import customtkinter as ctk
ctk.set_appearance_mode("dark")


#funções------------

def calcular():
    n1 = float(priunidade.get())
    n2 = float(segunidade.get())
    n3 = float(terunidade.get())

    try:
        media = (n1+n2+n3)/3
        
        if (media>=5):
            resultado.configure(text=f"A média final foi de {media:.1f} você foi aprovado")
        else:
            resultado.configure(text=f"A média final foi de {media:.1f} você foi aprovado")
    except:
        resultado.configure(text="Dado inválido")


#janela-----------

janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False, False)
janela.title("Sistema Escolar")
janela.iconbitmap("escola/3069198-cap-education-hat-school_112714.png")


#corpo da janela
titulo = ctk.CTkLabel(janela,
                    text= "Sistema Escolar",
                    text_color="yellow",
                    font=("Arial", 45,("bold"))
)
titulo.pack(pady=20)

priunidade = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color="yellow",
                        placeholder_text="digite a sua nota na 1ª Unidade"
)
priunidade.pack(pady=15)

segunidade = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color="yellow",
                        placeholder_text="digite a sua nota na 2ª Unidade")
segunidade.pack(pady=15)

terunidade = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color="yellow",
                        placeholder_text="digite a sua nota na 3ª Unidade")
terunidade.pack(pady=15)

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text="Calcular",
                    cursor= "heart",
                    fg_color="#f0ec04",
                    text_color="#020000",
                    font=("arial", 15, 'bold'),
                    hover_color="#554c18ff",
                    border_width=2,
                    border_color='',
                    command=calcular)
botao.pack(pady=10)


resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('Arial', 20))
resultado.pack(pady=10)

janela.mainloop()