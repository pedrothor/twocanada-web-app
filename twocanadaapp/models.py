from django.db import models


class VideosYoutube(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    imagem = models.CharField(max_length=300, null=False, blank=False)
    video_id = models.CharField(max_length=150, null=False, blank=False)

    class Meta:
        db_table = 'videos_youtube'
        verbose_name = 'video_youtube'
        verbose_name_plural = 'videos_youtube'


class Parceiros(models.Model):
    site_oficial = models.CharField(max_length=200, null=False, blank=False)
    imagem = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        db_table = 'parceiros'
        verbose_name = 'parceiro'
        verbose_name_plural = 'parceiros'


class Sobre(models.Model):
    texto = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        db_table = 'sobre'
        verbose_name = 'sobre'
        verbose_name_plural = 'sobre'


class Tcexp(models.Model):
    texto = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'tcexp'
        verbose_name = 'tcexp'
        verbose_name_plural = 'tcexp'


class Podcast(models.Model):
    texto = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        db_table = 'podcast'
        verbose_name = 'podcast'
        verbose_name_plural = 'podcast'