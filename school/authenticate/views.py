from asyncio import FastChildWatcher
from distutils.log import error
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages

from authenticate.forms import UserForm
from authenticate.models import User
# from django.contrib.auth.models import User

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
    login_msg = None
    if(request.method == 'POST'):
        
        # Note: left side  is the name of attribute of the database table
        # Noter: right side is the name of field

        # now, getting each data from each field
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']

        
        last_name = request.POST['lastName']
        contact = request.POST['contact']

        
        role = request.POST['role']
        username = request.POST['username']

        password = request.POST['password']
        confimPassword = request.POST['confirmPassword']
                
        form = UserForm(request.POST, request.FILES)


        # validation

        error_msg = None
        

        # check provied contact detail is number/digit or not
        for digit in contact:
            if digit.isdigit():
                validContact = True
            else:
                validContact = False

        # make restrictions (server side validation)

        if len(first_name) <= 3 or len(last_name) <= 3:
            error_msg = "First or last names cannot be lesser than 2 character."
            
        elif role == "Choose role":
            error_msg = "Choose role as admin, student or teacher."

        elif not validContact:
             error_msg = "* Contact cannot be alphabets."

        elif len(password) <= 5:
            error_msg = "Password cannot be lesser than 6 character."

        elif password != confimPassword:
            error_msg = "Password and Confrim password does not match."

        # if there is no error, which means valid info are provided
        if not error_msg:
            # saving content into the database

            if middle_name == '':
                middle_name = None
            
            # first_name is the attribute of the table
            # firstName is the name of the field

            User( 
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name,
                contact = contact,
                role = role,
                username = username, 
                password = password
            ).save()

            
            login_msg = first_name + ", your account has been created successfully. Now login."
            print(login_msg)

            return redirect("/home/home", {'message': login_msg})

        else : 
            return render(request, "authenticate/register.html", {'error': error_msg})


    return render(request, "authenticate/register.html")