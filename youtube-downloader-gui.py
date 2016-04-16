#!/usr/bin/env python3

from tkinter import Tk, Label, Entry, Button
from downloader import download_video

# cria uma janela
window = TK()

# seta o título da janela
window.title("Youtube Downloader")

# seta o tamanho da janela
window.geometry('500x200')

# não permite redimensionamento da janela
window.resizable(0,0)

# label do título do programa
title = Label(window, text ='Youtube Downloader', font=('Arial', 25) fg ='Blue')
title.pack()

# label da mensagem de execução do programa
msg = Label(window, text = '', font =('Arial', 15))

# cria uma entrada de texto para inserir a URL
entrey_url = Entry(window, width =60, justify ='center')

# seta o texto
entry_url.insert(0,'Colo sua URL aqui: ')

# chama o gerenciador de geometria
entry_name_video.pack()

# obtém o foco para a entrada de texto


# cria uma entrada de texto para inserir um nome para o vídeo


# seta o texto
entry_name_video = Entry(window, width =60, justify ='center')

# chama o gerenciador de geometria
# função para o evento de clique do botão
def click_button():
	url = entry_url.get()
	video_video = entry_name_video.get()
	
	if downloader_video(url, name_video)
		msg['fg'] = 'Green'
		msg['text'] = 'Download feito com sucesso!'
# cria um botão


# exibe a mensagem


# loop principal da aplicação


