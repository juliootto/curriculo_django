from django.shortcuts import render
from curriculo.models import Cursos, ExperienciaProficional, Escolaridade, Contato, Interesses


# Create your views here.
def index(request):
    cursos = Cursos.objects.all().order_by('-fim')
    experiencia = ExperienciaProficional.objects.all().order_by('-inicio')
    escolaridade = Escolaridade.objects.all().order_by('-inicio')
    interesses = Interesses.objects.all().order_by('-id')

    return render(request, 'index.html', { 'cursos': cursos,
                                            'experiencia': experiencia,
                                            'escolaridade': escolaridade,
                                            'interesses': interesses,                                            
                                        })

