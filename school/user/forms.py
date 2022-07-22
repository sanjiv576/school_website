from dataclasses import field
from django import forms
from user.models import Notice_Vacancy


class NoticeForm(forms.ModelForm):
    class Meta:
        # mentioning this is for notice
        model = Notice_Vacancy
        # for mapping with db
        fields = "__all__"