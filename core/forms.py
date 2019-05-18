from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    AC_CHOICES = (
        ('Bidder', 'Bidder'),
        ('Seller', 'Seller'),
    )
    company_name = forms.Field()
    account_type = forms.ChoiceField(help_text='Pick one', choices=AC_CHOICES)
    email = forms.EmailField(required=True, help_text='Valid email format: a@b.c')

    class Meta:
        model = User
        fields = ('username', 'company_name', 'email', 'account_type', 'password1', 'password2', )
