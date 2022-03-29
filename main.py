from download import download_video_audio, download_audio, download_video
from tkinter import *

#Construindo Janela
main_frame = Tk()

main_frame.title('Youtube Download')

main_frame.geometry('400x300')

main_title = Label(main_frame, text= 'Insira a url do Vídeo:', width= 50, height=3)
main_title.grid(column=0, row=0)

url_video_input = Entry(main_frame, width=40)
url_video_input.grid(column=0, row=1)

def get_url_video():
    url = url_video_input.get()
    download_video(url)
    status_download['text'] = 'Download concluído'

def get_url_audio():
    url = url_video_input.get()
    download_audio(url)
    status_download['text'] = 'Download concluído'

def get_url_video_audio():
    url = url_video_input.get()
    download_video_audio(url)
    status_download['text'] = 'Download concluído'

choose_options = Label(main_frame, text = 'Escolha um opção de Download:', height=3)
choose_options.grid(column=0, row=2)

button_video = Button(main_frame, text = 'Vídeo', command = get_url_video)
button_video.grid(column=0, row=3, pady=10)
button_audio = Button(main_frame, text = 'Áudio', command = get_url_audio)
button_audio.grid(column=0, row=4, pady=10)
button_video_audio = Button(main_frame, text = 'Vídeo e Áudio', command = get_url_video_audio)
button_video_audio.grid(column=0, row=5, pady=10)

status_download = Label(main_frame, text = '')
status_download.grid(column=0, row= 6)
status_download['text'] = ''

main_frame.mainloop()