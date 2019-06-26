# from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from django.conf import settings

from accounts.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # password = forms.CharField(min_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
