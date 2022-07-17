

from dataclasses import field
from django import forms
from authenticate.models import User


class UserForm(forms.ModelForm):
    class Meta:
        # mentioning this is for user
        model = User
        # for mapping with db
        fields = "__all__"