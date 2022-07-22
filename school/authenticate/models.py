import datetime
from unicodedata import category
from django.db import models

# Create your models here.

# models for UserInfo
class UserInfo(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key = True)
    first_name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=20, default="", null=True)
    last_name = models.CharField(max_length=20, null=False)
    contact = models.CharField(max_length=10, null=False, unique=True)
    role = models.CharField(max_length=10, null=False, default='')
    image = models.FileField(upload_to="static/images/user", default="default.jpg")
    username = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=160, null=False)
    

    class Meta:
        db_table = "UserInfo"
    

    def __str__(self):
        return "%s %s" % (self.user_id, self.first_name)

