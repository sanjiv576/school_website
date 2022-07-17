import datetime
from unicodedata import category
from django.db import models

# Create your models here.

# models for user
class User(models.Model):
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
        db_table = "user"

# class Notice_Academic(models.Model):
#     notice_id = models.AutoField(auto_created=True, primary_key = True)
#     title = models.CharField(max_length=30)
#     publish_date = models.CharField(models.DateTime, max_length=20, default=datetime.utcnow)
#     image = models.FileField(upload_to="static/images/user", default="default.jpg")
#     description = models.CharField(max_length=80, null=False)
#     category = models.CharField(max_length=30, null=False)
#     user_id = models.ForeignKey(User, default=None)

#     class Meta:
#         db_table = "notice_academic"