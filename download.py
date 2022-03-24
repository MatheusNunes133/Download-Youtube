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