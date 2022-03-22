from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('Bienvenidos')

def plantilla(request):
    template = loader.get_template('plantilla.html')
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre':'Jonathan'
    }
    plantilla_generada = template.render({})
    return HttpResponse(plantilla_generada)

    

