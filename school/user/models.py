from django.db import models
from authenticate.models import UserInfo
import datetime


# model for notice and vacancy
class Notice_Vacancy(models.Model):
    notice_id = models.AutoField(auto_created=True, primary_key = True)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30, null=False)
    publish_date = models.DateField()
    post_image = models.FileField(upload_to="static/images/user", default="default.png")
    description = models.TextField(max_length=200, null=False)
    
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Notice_Vacancy"