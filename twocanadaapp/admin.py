from django.contrib import admin
from .models import Parceiros, Sobre, Tcexp, Podcast


@admin.register(Parceiros)
class ParceirosAdmin(admin.ModelAdmin):
    pass


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    pass


@admin.register(Tcexp)
class TcexpAdmin(admin.ModelAdmin):
    pass


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    pass
