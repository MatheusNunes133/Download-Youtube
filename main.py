from pytube import YouTube

#Faz download do vídeo
def download_video(url):
    video = YouTube(url)
    title_video = video.title

    download_video = video.streams.get_highest_resolution()
    download_video.download(filename = 'Video_' + title_video + '.mp4')

#Faz download do áudio
def download_audio(url):
    video = YouTube(url)
    title_audio = video.title

    download_audio = video.streams.filter(only_audio = True)[0]
    download_audio.download(filename = 'Audio_' + title_audio + '.mp3')

#Faz download do vídeo e do áudio
def download_video_audio(url):
    video = YouTube(url)
    title = video.title

    download_video = video.streams.get_highest_resolution()
    download_video.download(filename = 'Video_' + title + '.mp4')
    
    download_audio = video.streams.filter(only_audio = True)[0]
    download_audio.download(filename = 'Audio_' + title + '.mp3')

#Menu de opções
controls_while = True
while controls_while:
    print('\nEscolha 1 para fazer o download de um vídeo')
    print('Escolha 2 para fazer o download de um áudio')
    print('Escolha 3 para fazer o download de um vídeo e de um áudio')
    print('Escolha 0 para sair')

    choose = int(input('Informe sua escolha:'))

    if choose == 1:
        url = str(input('Informe a url do vídeo:'))
        download_video(url)
        print('\nDownload concluido!\n')
    elif choose == 2:
        url = str(input('Informe a url do vídeo:'))
        download_audio(url)
        print('\nDownload concluido!\n')
    elif choose == 3:
        url = str(input('Informe a url do vídeo:'))
        download_video_audio(url)
        print('\nDownload concluido!\n')
    elif choose == 0:
        controls_while = False
    else:
        print('Não existe essa escolha!')