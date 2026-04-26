from portal.models import Artigo, Evento, Autor

def get_context(extra_context=None):
    context = {
        'total_artigos': Artigo.objects.filter(status='DIS').count(),
        'total_eventos': Evento.objects.filter(status='DIS').count(),
        'total_autores': Autor.objects.count(),
        'status_artigo': Artigo.objects.filter(status='DIS').order_by('criado_em').last().criado_em,
        'status_evento': Evento.objects.filter(status='DIS').order_by('criado_em').last().criado_em,
        'status_autor': Autor.objects.order_by('criado_em').last().criado_em,
    }
    if extra_context:
        context.update(extra_context)
    return context