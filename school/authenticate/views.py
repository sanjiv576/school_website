from django.shortcuts import render

# Create your views here.


def login_page(request):
    print("hello, checking validation")
    return render(request, 'home/homepage.html')


def register_page(request):
    print("This is register")
    return render(request, "authenticate/register.html")