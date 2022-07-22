from dataclasses import field
from django import forms
from customer.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        # mentioning this is for notice
        model = Appointment
        # for mapping with db
        fields = "__all__"