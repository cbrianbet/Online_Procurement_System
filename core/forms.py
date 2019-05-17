from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    company_name = forms.Field()
    account_type = forms.Field(help_text='Pick one')
    email = forms.EmailField(required=True, help_text='Valid email format: a@b.c')

    class Meta:
        model = User
        fields = ('username', 'company_name', 'email', 'account_type', 'password1', 'password2', )
