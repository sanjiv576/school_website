from unicodedata import category
from django.shortcuts import render
from customer.models import Appointment
def appointment(request):

    if(request.method == 'POST'):
        data = request.POST

        fullName = data.get('full_name')
        category = data.get('category')
        contact = data.get('contact')
        date = data.get('date')
        time = data.get('time')
        description = data.get('description')

        Appointment(fullName = fullName, category = category, contact = contact, date = date,
        time = time, description = description).save()

        success_msg = "Your appointment has been scheduled. Please, visit office."

        return render(request, "home/homepage.html", {'message': success_msg})

    return render(request, 'customer/appointment.html')



