from dataclasses import field
from django import forms
from user.models import Notice_Vacancy, Intro


class NoticeForm(forms.ModelForm):
    class Meta:
        # mentioning this is for notice
        model = Notice_Vacancy
        # for mapping with db
        fields = "__all__"

class IntroForm(forms.ModelForm):
    class Meta:
        
        model = Intro
        fields = "__all__"