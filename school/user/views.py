from datetime import datetime
from unicodedata import category
from django.shortcuts import render, redirect
from authenticate.models import UserInfo
from user.models import Notice_Vacancy, Intro
from user.forms import NoticeForm, IntroForm
from authenticate.forms import UserForm
from django.contrib.auth.decorators import login_required
# opens admin panel and shows data 

@login_required(login_url='/home/home')
def adminPanel(request):

    users = UserInfo.objects.all()
    notice_details = Notice_Vacancy.objects.all()
    # return render(request, 'user/adminDashboard.html', {'users': users}, {'notice_details': notice_details})
    return render(request, 'user/adminDashboard.html', {'users': users})


def viewNotice(request):
    notice_details = Notice_Vacancy.objects.all()
    return render(request, 'user/adminDashboard.html', {'notice_details': notice_details})

@login_required(login_url='/home/home')
def viewCustomer(request):
    users = UserInfo.objects.all()
    return render(request, 'user/adminDashboard.html', {'users': users})

@login_required(login_url='/home/home')
def viewAppointment(request):

    # here appointment required not notice
    notice_details = Notice_Vacancy.objects.all()
    return render(request, 'user/adminDashboard.html', {'notice_details': notice_details})

@login_required(login_url='/home/home')
def viewIntro(request):
    
    intros = Intro.objects.all()
    return render(request, 'user/adminDashboard.html', {'intros': intros})


# save notice_vacancy
@login_required(login_url='/home/home')
def addNotice(request):
    print("This is adding notice section/function")
    print(request.method)

    success_msg = None
    
    if(request.method == 'POST'):

        # mapping with database
        data = Notice_Vacancy(request.POST, request.FILES)

        totalPost = len(Notice_Vacancy.objects.all())
        print(totalPost)
        title = request.POST['title']
        publish_date = datetime.date(datetime.now())
        category = request.POST['category']
        # post_image = request.POST['post_image']
        description = request.POST['description']
        print(publish_date)

        saving = Notice_Vacancy(
            title = title,
            publish_date = publish_date,
            category = category,
            # post_image = post_image,
            description = description

        ).save()
        print(saving)

        

        success_msg = "Your post has been successfully published ."

        return render(request, "user/adminDashboard.html", {'messages': success_msg})
        # print(publish_date)
        # print(title)
        # print(category)
        # print(description)
        # print(request.FILES)
        # print(data)

    # if not success_msg:
    #     error_msg = "Something went wrong. Try again."
    return render(request, 'user/addNotice.html')

# save recently added introduction section

@login_required(login_url='/home/home')
def addIntro(request):


    success_msg = None
    
    if(request.method == 'POST'):

        totalPost = len(Intro.objects.all())

        intro_title = request.POST['intro_title']
        # intro_image = request.POST['intro_image']
        # intro_image = request.POST.get('intro_image', False)
        intro_description = request.POST['intro_desc']
        
        

        Intro(
            intro_title = intro_title,
            # intro_image = intro_image,
            intro_description = intro_description,
            

        ).save()

        

        success_msg = "Introduction section has been successfully published ."

        return render(request, "user/adminDashboard.html", {'messages': success_msg})
    return render(request, 'user/addIntro.html')



# for editing logic

@login_required(login_url='/home/home')
def editNotice(request, c_id):
    
    data = Notice_Vacancy.objects.get(notice_id=c_id)
    return render(request, "user/editNotice.html", {'data': data})


# for editing logic
def editIntro(request, c_id):
    print(f"{c_id} is the id")
    data = Intro.objects.get(intro_id=c_id)
    print(data)
    return render(request, "user/editIntro.html", {'data': data})



# for updating logic

@login_required(login_url='/home/home')
def updateIntro(request, c_id):

    success_msg = None
    
    if(request.method == 'POST'):

        totalPost = len(Intro.objects.all())

        intro_title = request.POST['intro_title']
        # intro_image = request.POST['intro_image']
        # intro_image = request.POST.get('intro_image', False)
        intro_description = request.POST['intro_desc']
        
        updateInfo = Intro.objects.get(intro_id=c_id)
        updateInfo.intro_title = intro_title
        updateInfo.intro_description = intro_description
        updateInfo.save()
    
        success_msg = "Introduction section has been successfully updated ."

        return render(request, "user/adminDashboard.html", {'messages': success_msg})

@login_required(login_url='/home/home')
def updateNotice(request, c_id):

    success_msg = None
    
    if(request.method == 'POST'):

        totalPost = len(Notice_Vacancy.objects.all())

        title = request.POST['title']
        publish_date = datetime.date(datetime.now())
        category = request.POST['category']
        # post_image = request.POST['post_image']
        description = request.POST['description']
        
        
        updateInfo = Notice_Vacancy.objects.get(notice_id=c_id)
        updateInfo.title = title
        updateInfo.publish_date = publish_date
        updateInfo.category = category
        updateInfo.description = description
        updateInfo.save()
    
        success_msg = "Notice has been successfully updated."

        return render(request, "user/adminDashboard.html", {'messages': success_msg})

# delete from the database

@login_required(login_url='/home/home')
def deleteIntro(request, c_id):

    data = Intro.objects.get(intro_id=c_id)
    data.delete()

    success_msg = "Deleted successfully."

    return render(request, "user/adminDashboard.html", {'messages': success_msg})


@login_required(login_url='/home/home')
def deleteNotice(request, c_id):

    data = Notice_Vacancy.objects.get(notice_id=c_id)
    data.delete()

    success_msg = "Deleted successfully."

    return render(request, "user/adminDashboard.html", {'messages': success_msg})

    