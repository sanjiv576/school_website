from datetime import datetime
from unicodedata import category
from django.shortcuts import render, redirect
from authenticate.models import UserInfo
from user.models import Notice_Vacancy
from user.forms import NoticeForm
from authenticate.forms import UserForm

# opens admin panel and shows data 
def adminPanel(request):

    users = UserInfo.objects.all()
    return render(request, 'user/adminDashboard.html', {'users': users})

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

def addIntro(request):
    return render(request, 'user/addIntro.html')