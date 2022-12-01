from django.shortcuts import render
from .models import *


# Create your views here.

def homepage(request):
    article  = news.objects.all()
    context  = {
        'article': article
    }
    return render(request, 'index.html', context)