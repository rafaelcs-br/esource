from django.shortcuts import render
from portal.models import Artigo

# Create your views here.
def artigos(request):
    artigos = Artigo.objects.all().filter(status='DIS')
    
    context = {
        'artigos': artigos
    }
    
    return render(request, 'artigos.html', context)