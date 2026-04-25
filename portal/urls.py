from django.urls import path
from portal import views

app_name = 'portal'

urlpatterns = [
    path('', views.artigos, name='home'),
    path('artigos', views.artigos, name='artigos'),
    path('artigos/<int:artigo_id>', views.detalhes_artigo, name='detalhes_artigo'),
    path('eventos', views.eventos, name='eventos'),
    path('autores', views.autores, name='autores'),
]