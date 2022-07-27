from django.shortcuts import render
from core.models import Evento


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    # evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)
