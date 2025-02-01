from .models import CustomUser
from django import forms 
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Username",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        label="Email"
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Password"
    )


    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Confirm Password"
    )
    class Meta:
        model = CustomUser

        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Tell us about yourself",
            "rows": 3
        }),
        label="Bio",
        required=False
    )
    profile_picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = CustomUser

        
        fields = ('bio',
                'profile_picture'
                )


class CustomAuthenticationform(AuthenticationForm):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Username",
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="password"
    )
