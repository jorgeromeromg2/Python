#------CONVERTENDO VIDEO E BAIXANDO PELO PYHON -----
from pytube import YouTube
link = input('digite o url do youtube: ')
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)

print('entre com a opção do formato')
dn_option = int(input('Digite a opção: '))
dn_video = videos[dn_option]
dn_video.download()
print('Download com sucesso')
