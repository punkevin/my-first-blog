from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Convocatoria
from .forms import ConvForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'GestionConvocatoria/post_list.html', {'convocatorias': convocatorias})

def conv_detail(request, pk):
    convocatorias = get_object_or_404(Convocatoria, pk=pk)
    return render(request, 'GestionConvocatoria/conv_detail.html', {'convocatorias': convocatorias})

#def conv_new(request):
#    form = ConvForm()
#    return render(request, 'GestionConvocatoria/conv_edit.html', {'form': form})

def conv_new(request):
    if request.method == "POST":
        form = ConvForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            conv = form.save(commit=False)
            conv.save()
            return redirect('conv_detail', pk=conv.pk)
    else:
        form = ConvForm()
    return render(request, 'GestionConvocatoria/conv_edit.html', {'form': form})

def conv_edit(request, pk):
    conv = get_object_or_404(Convocatoria, pk=pk)
    if request.method == "POST":
        form = ConvForm(request.POST, instance=conv)
        if form.is_valid():
            conv = form.save(commit=False)
            conv.save()
            return redirect('conv_detail', pk=conv.pk)
    else:
        form = ConvForm(instance=conv)
    return render(request, 'GestionConvocatoria/conv_edit.html', {'form': form})
