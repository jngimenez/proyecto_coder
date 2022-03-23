from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'index/index.html', {})

def plantilla(request):
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Jonathan',
        'apellido': 'Gimenez'
    }    
    return render(request, 'index/plantilla.html', datos)

    

