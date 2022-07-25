
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from authenticate.views import *
# for testing view
from authenticate.models import UserInfo
from django.contrib.auth.models import User

class testViews(TestCase):
    def test_index(self):
        user = User.objects.create(username="testing")
        user.set_password('1234567')
        user.save()

        client = Client()
        logged_in = client.login(username='testing', password='1234567')
        response = client.get(reverse(login_page))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/homepage.html')

        
    # testing create
    def test_create_user(self):
        user = User.objects.create(username="testing")
        user.set_password('1234567')
        user.save()

        client = Client()
        logged_in = client.login(username='testing', password='1234567')
        response = client.post(reverse(register_page),{
            'first_name': 'testing_name',
            'last_name': 'testing_last_name',
            'username': 'testing_',
            'password': '1234567'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/user/admin')
