from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def single(request):
    return render(request, "blog-single.html")


def portfolio(request):
    return render(request, "portfolio-details.html")
