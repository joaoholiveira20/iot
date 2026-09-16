import customtkinter as ctk 
ctk.set_appearance_mode("dark")

#funções---------------

def calcular():
    d = float(dstviagem.get())
    c = float(consumo.get())
    p = float(precoatual.get())
    
    formula = (d/c)*p
    
    resultado.configure(text=f'O valor para a viagem é de R$ {formula:.2f}')

#janela------

janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("APP VIAGEM")
janela.iconbitmap("iot/interface/car_13260.png")

#corpo da janela
titulo = ctk.CTkLabel(janela,
                text= "APP VIAGEM",
                text_color="white",
                font=("Verdanna", 35,('bold'))
    )
titulo.pack(pady=20)
    
dstviagem = ctk.CTkEntry(janela,
                    width=300,
                    height=40,
                    border_color="white",
                    placeholder_text="Digite a distancia da viagem em KM")
dstviagem.pack(pady=20)

consumo = ctk.CTkEntry(janela,
                        width=300,
                        height=40,
                        border_color="white",
                        placeholder_text="Digite o consumo do seu veiculo")
consumo.pack(pady=20)

precoatual = ctk.CTkEntry(janela,
                        width=300,
                        height=40,
                        border_color="white",
                        placeholder_text="Digite o prço atual do combustivel")
precoatual.pack(pady=20)

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text="Calcular Gasto",
                    fg_color="#97f577",
                    text_color="#ffffff",
                    cursor= "heart",
                    font=("arial", 30),
                    border_width=2,
                    border_color='',
                    command=calcular)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial', 20))
resultado.pack(pady=10)

janela.mainloop()
