
from dataclasses import field
from django import forms
from authenticate.models import UserInfo


class UserForm(forms.ModelForm):
    class Meta:
        # mentioning this is for user
        model = UserInfo
        # for mapping with db
        fields = "__all__"