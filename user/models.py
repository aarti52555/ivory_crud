from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for ivory_crud.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)


class Registration(models.Model):
    """
    custom model for the CRUD Operation.
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    full_name = CharField(max_length=50, null=True, blank=True)
    email = EmailField(max_length=255, unique=True)
    gender = CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    address = CharField(max_length=255, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    state = CharField(max_length=50, null=True, blank=True)
    country = CharField(max_length=50, null=True, blank=True)
    pin_code = CharField(max_length=6, null=True, blank=True)
    contact_number = CharField(max_length=10, null=True, blank=True)
    education_qualification = CharField(max_length=50, null=True, blank=True)
    designation = CharField(max_length=50, null=True, blank=True)


