from django.shortcuts import render
from curriculo.models import Cursos

# Create your views here.
def index(request):
    cursos = Cursos.objects.all().order_by('-fim')
    return render(request, 'index.html', {'cursos': cursos})

