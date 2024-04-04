from django.shortcuts import render

def index(request):
    return render(request, 'main51/index.html')

def about(request):
    return render(request, 'main51/about.html')