from tkinter import NO
from urllib import response
from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase, Client

# for url testing
from user.views import addNotice, addIntro, editNotice, editIntro, deleteIntro, deleteNotice

# for view testing
from user.models import Notice_Vacancy, Intro

#  testing url 
class TestUrls(SimpleTestCase):

    # testing url of addNotice which creates notice or vacancy
    def test_create_urls(self):
        # reverse --> finds url
        url = reverse(addNotice)
        
        # resolve --> helps to get the function of that url 

        self.assertEquals(resolve(url).func, addNotice)

    # testing url of addIntor which creates introduction
    def test_create_intro_urls(self):
        url = reverse(addIntro)
        self.assertEquals(resolve(url).func, addIntro)

    # testing url of edit code of editNotice
    def test_edit_notice_urls(self):
        url = reverse(editNotice, args='1')
        self.assertEquals(resolve(url).func, editNotice)

    
    # testing url of edit code of  editIntro
    def test_edit_intro_urls(self):
        url = reverse(editIntro, args='1')
        self.assertEquals(resolve(url).func, editIntro)


# testing delete function
class testViews(TestCase):

    # testing deleteIntro function
    def test_delete_intro(self):

        intro = Intro.objects.create(intro_title = "Introduction", intro_description = "KEBS School is ..." )
        # print(intro.intro_id)
        client = Client()
        response = client.delete(reverse(deleteIntro, args='2'))
        self.assertEquals(response.status_code,302)

    # testing deleteNotice function
    def test_delete_notice(self):

        notice = Notice_Vacancy.objects.create(
            title = "Exam",
            category = "notice",
            publish_date = "2022-07-12",
            post_image = "default.png",
            description = "From 20 July, exam starts." )

        # print(notice.notice_id)

        client = Client()
        response = client.delete(reverse(deleteNotice, args='2'))
        self.assertEquals(response.status_code,302)



