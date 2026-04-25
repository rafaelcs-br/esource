from django.shortcuts import render
from portal.models import Artigo, Evento, Autor

# Create your views here.
def artigos(request):
    artigos = Artigo.objects.all().filter(status='DIS')
    
    context = {
        'artigos': artigos
    }
    
    return render(request, 'artigos.html', context)

def eventos(request):
    eventos = Evento.objects.all().filter(status='DIS')
    
    context = {
        'eventos': eventos
    }
    
    return render(request, 'eventos.html', context)

def autores(request):
    autores = Autor.objects.all()
    
    context = {
        'autores': autores
    }
    
    return render(request, 'autores.html', context)