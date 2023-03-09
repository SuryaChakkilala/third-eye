from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    address = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    country = forms.CharField(max_length=150)
    is_doctor = forms.BooleanField(required=False)
    doctor_speciality = forms.CharField(max_length=200, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'city', 'country', 'is_doctor', 'doctor_speciality')

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    address = forms.CharField(max_length=150, required=False)
    city = forms.CharField(max_length=150)
    country = forms.CharField(max_length=150)
    is_doctor = forms.BooleanField(required=False)
    doctor_speciality = forms.CharField(max_length=200, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'is_doctor', 'doctor_speciality')