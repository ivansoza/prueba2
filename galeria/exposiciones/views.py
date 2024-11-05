from django.shortcuts import render
from django.http import HttpResponse


def ver_exposiciones(request):
    return HttpResponse("Lista de exposiciones actuales y pasadas")



def ver_exposiciones_futuras(request):
    return HttpResponse("Lista de exposiciones futuras")

def eliminar_exposiciones(request):
    return HttpResponse("eliminar exposiciones")



