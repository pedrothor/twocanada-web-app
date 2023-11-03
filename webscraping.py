from googleapiclient.discovery import build
from twocanadaapp.models import VideosYoutube


def varredura_youtube():
    youTubeKey = ''
    youtube = build('youtube', 'v3', developerKey=youTubeKey)

    # ID da playlist (código após a palavra 'list' na url da playlist)
    playlistId = 'PL_vS95-NEpwbm3Y8JAQYPx1AZUBThkGja'

    # nome da playlist
    playlistName = 'TwoCanada Podcast'

    # necessário em caso de + de 50 vídeos na playlist e queira pegar todos
    nextPage_token = None

    playlist_videos = []
    info_videos = []

    while True:

        # encapsulando todas as informações da playlist
        res = youtube.playlistItems().list(part='snippet', playlistId=playlistId, maxResults=50, pageToken=nextPage_token).execute()

        # armazenando todos os vídeos
        playlist_videos += res['items']

        # verificando se há mais de uma página, visto que 1 página armazena 50 vídeos
        nextPage_token = res.get('nextPageToken')

        for k in playlist_videos[-5::]:
            informacoes = k['snippet']

            # pegando o título
            titulo = informacoes['title'].lower()

            # pegando a thumbnail com width 320 e height 180
            thumbnail = informacoes['thumbnails']['medium']['url']

            # pegando a id do vídeo
            video_id = informacoes['resourceId']['videoId']

            info_videos.append(dict(titulo=titulo, thumbnail=thumbnail, video_id=video_id))

        if nextPage_token is None:
            break

    return info_videos


