from django.contrib import admin
from portal.models import Evento, Autor, Subarea, Artigo

# Register your models here.
admin.site.register(Evento)
admin.site.register(Autor)
admin.site.register(Subarea)
admin.site.register(Artigo)