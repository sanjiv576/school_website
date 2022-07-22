from django.shortcuts import render

def appointment(request):
    return render(request, 'customer/appointment.html')
