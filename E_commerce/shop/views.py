from django.shortcuts import render
from django.http import HttpResponse

from .models import Student


# Create your views here.

def home(request):
    return render(request, 'homee.html')


def dob(request):
    return render(request, 'dob.html')


def clas(request):
    return render(request, 'class.html')


def adm(request):
    return render(request, 'adm.html')


def namee(request):
    return render(request, 'name.html')


def students_list(request):
    student = Student.objects.all()
    return render(request, 'students list.html', {"students": student})
