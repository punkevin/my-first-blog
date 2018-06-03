from django.shortcuts import render
from django.utils import timezone
from .models import Convocatoria

# Create your views here.

def post_list(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'GestionConvocatoria/post_list.html', {'convocatorias': convocatorias})
