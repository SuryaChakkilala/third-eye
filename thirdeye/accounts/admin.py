from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .forms import CustomUserChangeForm
from import_export.admin import ImportExportModelAdmin


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

admin.site.register(CustomUser)