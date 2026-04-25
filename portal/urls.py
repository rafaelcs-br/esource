from django.urls import path
from portal import views

app_name = 'portal'

urlpatterns = [
    path('', views.artigos, name='home'),
    path('artigos', views.artigos, name='artigos'),
    path('eventos', views.eventos, name='eventos'),
    path('autores', views.autores, name='autores'),
]