from django.shortcuts import render

from .models import VideosYoutube, Parceiros, Sobre, Tcexp, Podcast
from pathlib import Path


def index(request):

    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    # último vídeo diretamente do youtube
    # ultimo_video_youtube = varredura_youtube()[-1]
    #
    # # titulo do último vídeo
    # titulo_ultimo_video = ultimo_video_youtube['titulo']
    #
    # # se título do último vídeo da playlist for diferente do título do último vídeo cadastrado no banco de dados...
    # if titulo_ultimo_video != VideosYoutube.objects.last().nome:
    #
    #     # deletando o primeiro (para manter sempre 5 salvos)
    #     VideosYoutube.objects.first().delete()
    #
    #     # criando novo objeto no model (para manter sempre 5 salvos)
    #     video_novo = VideosYoutube.objects.create(nome=titulo_ultimo_video, imagem=ultimo_video_youtube['thumbnail'], video_id=ultimo_video_youtube['video_id'])
    #     video_novo.save()

    videos_db = VideosYoutube.objects.all().order_by('-id')
    parceiros = Parceiros.objects.all()
    sobre = Sobre.objects.all()
    tcexp = Tcexp.objects.all()
    podcast = Podcast.objects.all()

    context = {
        'videos_db': videos_db,
        'parceiros': parceiros,
        'sobre': sobre,
        'tcexp': tcexp,
        'podcast': podcast,
               }

    return render(request, 'index.html', context)

