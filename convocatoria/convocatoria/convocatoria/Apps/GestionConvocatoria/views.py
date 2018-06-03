from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Convocatoria

# Create your views here.

def post_list(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'GestionConvocatoria/post_list.html', {'convocatorias': convocatorias})

def conv_detail(request, pk):
    convocatorias = get_object_or_404(Convocatoria, pk=pk)
    return render(request, 'GestionConvocatoria/conv_detail.html', {'convocatorias': convocatorias})
