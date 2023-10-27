from django.shortcuts import render
from django.http import *
from .models import block_posts


def index(request):
    model = block_posts.objects.get(id=1)
    return render(request, "index.html", context={'model': model})


def map_page(request):
    model = block_posts.objects.get(id=2)
    return render(request, "map_page.html", context={'model': model})

