from django.db import models
from authenticate.models import UserInfo



# model for notice and vacancy
class Appointment(models.Model):
    appointment_id = models.AutoField(auto_created=True, primary_key = True)
    fullName = models.CharField(max_length=40, null=False)
    contact = models.CharField(max_length=10, null=False)
    category = models.CharField(max_length=30, null=False)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=200, null=False)
    
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Appointment"