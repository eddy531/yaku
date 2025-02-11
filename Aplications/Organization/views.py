from django.shortcuts import render
from .models import Comunicado

def home(request):
    return render(request, 'home.html')