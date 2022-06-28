from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/homepage.html')


def register(request):
    return render(request, 'home/register.html')


def home(request):
    return render(request, "home/homepage.html")