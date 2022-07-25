from django.shortcuts import render
from user.models import Notice_Vacancy


# Create your views here.
def index(request):

    notice_details = Notice_Vacancy.objects.all()
    return render(request, 'home/homepage.html', {'notice_details': notice_details})


def home(request):
    
    notice_details = Notice_Vacancy.objects.all()
    return render(request, 'home/homepage.html', {'notice_details': notice_details})