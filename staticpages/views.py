from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<h1>Hello World!</h1>")
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)