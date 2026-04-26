from django.shortcuts import render, get_object_or_404
from portal.models import Artigo, Evento, Autor
from portal.utils.context import get_context

# Create your views here.
def artigos(request):
    artigos = Artigo.objects.all().filter(status='DIS')
    
    context = get_context({'artigos': artigos})
    
    return render(request, 'artigos.html', context)

def eventos(request):
    eventos = Evento.objects.all().filter(status='DIS')
    
    context = get_context({'eventos': eventos})
    
    return render(request, 'eventos.html', context)

def autores(request):
    autores = Autor.objects.all()
    
    context = get_context({'autores': autores})

    return render(request, 'autores.html', context)

def detalhes_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    context = {
        'artigo': artigo
    }
    
    return render(request, 'artigos/detalhes_artigo.html', context)