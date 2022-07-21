from asyncio import FastChildWatcher
from distutils.log import error
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages

from authenticate.forms import UserForm
from authenticate.models import UserInfo

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_page(request):
    
    print("hello, checking validation")
    print(request.method)
    # message = None
    if(request.method == 'POST'):
        error_msg = None

        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        user = authenticate(request,
                username=request.POST['username'],
                password = request.POST['password']
                )

        print(user)
        print("HEllo heloo")

        # if there is valid/registered account, then, login
        if(user is not None):
            # add login account details in django_session table of django
            login(request, user)
            message = "Login successfully"
            print(message)
            # open admin panel
            return redirect('/home/home')
        else :
            print("User account is not found")
            error_msg = "Provided account has not been registered or something went wrong."
            return render(request, 'home/homepage.html', {'error': error_msg})

    # messages.add_message(request, messages.INFO, 'Hello world.')
    # messages.success(request, 'Profile details updated.')
    # messages = messages.success(request, 'Profile details updated.')
    # messages = "Good job"

    messages.warning(request, "Login failed")
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

            UserInfo( 
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name,
                contact = contact,
                role = role,
                username = username, 
                password = password
            ).save()

            # for auth_user

            User.objects.create_user(
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            username = request.POST['username'],
            password = request.POST['password']
            )

            
            login_msg = first_name + ", your account has been created successfully. Now login."
            print(login_msg)

            return redirect("/home/home", {'message': login_msg})

        else : 
            return render(request, "authenticate/register.html", {'error': error_msg})


    return render(request, "authenticate/register.html")


def logout_func(request):
    # loggin out the user
    logout(request)

    login_msg = "You are loged out."

    print("User log out")
    return redirect("/home/home", {'message': login_msg})