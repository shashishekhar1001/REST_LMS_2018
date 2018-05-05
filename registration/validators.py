from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
import os

def validate_email(value):
    email_validator = EmailValidator()
    try:
        email_validator(value)
    except:
        raise ValidationError("Invalid Email.")

def existing_email_validator(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError("This email address is already registered.")
        
def invalid_email(value):
    if User.objects.filter(email=value).exists() == False:
        raise ValidationError("Email Does not exist.")

def image_file_validator(value):
    ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.bmp']
    if value:
        ext = os.path.splitext(value.name)[1]

    if (str(ext) in ALLOWED_EXTENSIONS):
        pass
    else:
        raise ValidationError("Please select an image of type:- ['jpg', 'jpeg', 'png', 'bmp']") 
