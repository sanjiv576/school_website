from django.shortcuts import render

# Create your views here.
def adminPanel(request):
    return render(request, 'user/adminDashboard.html')

def addNotice(request):
    return render(request, 'user/addNotice.html')

def addIntro(request):
    return render(request, 'user/addIntro.html')