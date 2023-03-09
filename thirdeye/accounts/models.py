from django.contrib.auth.models import AbstractUser
from django.db import models
from import_export.admin import ImportExportModelAdmin

class CustomUser(AbstractUser):
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    is_doctor = models.BooleanField(default=True)
    doctor_speciality = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username