from django.shortcuts import redirect, render

from .models import cerrajero
from . forms import cerrajeroformulario, CerrajeroBusqueda

# Create your views here.

def crear_cerrajero(request):
    if request.method=='POST':
        form = cerrajeroformulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            Cerrajero=cerrajero(nombre=data['nombre'], apellido=data['apellido'], desempleado=data['desempleado'])
            Cerrajero.save()
           # return render(request, 'index/index.html',{} )
            return redirect('index')
    form=cerrajeroformulario()
    return render(request, "profesionales/crear_cerrajero.html", {'form':form})


def lista_cerrajeros(request):
    nombre_a_buscar = request.GET.get('nombre', None)

    if nombre_a_buscar is not None:
        cerrajeros = cerrajero.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        cerrajeros= cerrajero.objects.all()

    form= CerrajeroBusqueda()
    return render(request, "profesionales/lista_cerrajeros.html", {'form':form})