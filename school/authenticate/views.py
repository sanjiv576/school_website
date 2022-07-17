from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages

from authenticate.forms import UserForm


def login_page(request):
    
    print("hello, checking validation")
    

    # messages.add_message(request, messages.INFO, 'Hello world.')
    # messages.success(request, 'Profile details updated.')
    # messages = messages.success(request, 'Profile details updated.')
    # messages = "Good job"

    messages.success(request, "Login successfully")
    return render(request, 'home/homepage.html')


def register_page(request):

    print("This is register")
    print(request.method)
    if(request.method == 'POST'):
        
        # Note: left side  is the name of attribute of the database table
        # Noter: right side is the name of field

        # now, validations
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']

        
        last_name = request.POST['lastName']
        contact = request.POST['contact']

        
        role = request.POST['role']
        username = request.POST['username']

        password = request.POST['password']
        confimPassword = request.POST['confirmPassword']
        
        # if(request.method == 'POST'):
        
        #     if(first_name.isnumeric() or first_name.isalnum()):
        #         messages.warning(request, "First name does not contdfsfsfain numbers")

        # print(role)
        print(role)

        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            print(form)
            return redirect("/home/index")


    return render(request, "authenticate/register.html")