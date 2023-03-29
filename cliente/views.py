from django.shortcuts import render
import requests
from django . http import HttpResponse

def buscar(request):
    api = requests.get("http://127.0.0.1:8000/api_cliente/?format=json")

    return HttpResponse(api)


def produto(request):
    api = requests.get("http://127.0.0.1:8000/api_produto/?format=json")

    return HttpResponse(api)