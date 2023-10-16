from django.shortcuts import render
from django.http import *


def index(request):
    return render(request, "index.html")


def map_page(request):
    return render(request, "map_page.html")

