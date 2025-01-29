from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Medida
from django.db import transaction

# Create your views here.

def medidas(request):
    medidas = Medida.objects.all()
    paginator = Paginator(medidas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = []
    for medida in page_obj:
        medida_data = {
            'id_medida': medida.id_medida,
            'nombre': medida.nombre,
        }
        data.append(medida_data)
        
    response = {
        'total': len(data),
        'medidas': data
    }
    
    return JsonResponse(response)