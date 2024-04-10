from televisão import Tv
import tkinter as tk

janela = tk.Tk()
janela.title("Controle Remoto da TV")
janela.configure(bg="#b2edde")

# Criando o objeto de controle da TV
controle_tv = Tv()

# Funções dos botões
def ligarDesligar():
    controle_tv.onOff()
    if not controle_tv.start:
        janela.destroy()

def aumentarVolume():
    controle_tv.upVolume()

def diminuirVolume():
    controle_tv.downVolume()

def aumentarCanal():
    controle_tv.upChannel()

def diminuirCanal():
    controle_tv.downChannel()

def mudarCanal(canal):
    controle_tv.levelChannel(canal)

def mutar():
    controle_tv.mute()

def info():
    controle_tv.info()


fonte_botoes = ("Arial Narrow", 14, 'bold') 
bg_botoes = "#cef0e7" 

botao_ligar_desligar = tk.Button(janela, text="Ligar/Desligar", font=fonte_botoes, bg=bg_botoes, command=ligarDesligar)
botao_ligar_desligar.grid(row=0, column=0, padx=6, pady=6)

botao_info = tk.Button(janela, text="INFO", font=fonte_botoes, bg=bg_botoes, command=info)
botao_info.grid(row=0, column=2, padx=4, pady=4)

botao_aumentar_volume = tk.Button(janela, text="Volume +", font=fonte_botoes, bg=bg_botoes, command=aumentarVolume)
botao_aumentar_volume.grid(row=1, column=0, padx=4, pady=4)

botao_diminuir_volume = tk.Button(janela, text="Volume -", font=fonte_botoes, bg=bg_botoes, command=diminuirVolume)
botao_diminuir_volume.grid(row=2, column=0, padx=4, pady=4)

botao_aumentar_Canal = tk.Button(janela, text="Canal +", font=fonte_botoes, bg=bg_botoes, command=aumentarCanal)
botao_aumentar_Canal.grid(row=1, column=2, padx=6, pady=6)

botao_diminuir_volume = tk.Button(janela, text="Canal -", font=fonte_botoes, bg=bg_botoes, command=diminuirCanal)
botao_diminuir_volume.grid(row=2, column=2, padx=6, pady=6)


botao_mudo = tk.Button(janela, text="Mudo", font=fonte_botoes, bg=bg_botoes, command=mutar)
botao_mudo.grid(row=2, column=1, padx=5, pady=5)


# Botões de mudar de canal
for i in range(1, 10):
    botao_canal = tk.Button(janela, text=f"{i}", font=fonte_botoes, bg=bg_botoes, command=lambda c=i: mudarCanal(c))
    botao_canal.grid(row=(i-1)//3+3, column=(i-1)%3, padx=4.5, pady=4.5)


janela.mainloop()