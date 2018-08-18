from django import forms
from .models import *
from .validators import validate_email, existing_email_validator, invalid_email, image_file_validator
from django.forms import ModelForm
from django.core.exceptions import ValidationError
import os

class CommonRegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    mobile = forms.CharField(max_length=20)
    email = forms.EmailField(required=True, validators=[validate_email, existing_email_validator])  
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    REGISTRATION_CHOICES = (
        ('Learner', 'Learner'),
        ('Trainer', 'Trainer'),
        ('Vendor', 'Vendor'),
        ('Client', 'Client'),
        ('Job Seeker', 'Job Seeker'),
    )
    register_as = forms.ChoiceField(choices=REGISTRATION_CHOICES, widget=forms.RadioSelect, required=True, label='Register As')

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label="Email", validators=[invalid_email])  
    password = forms.CharField(widget=forms.PasswordInput, required=True)

  
class UpdateTrainerProfileForm(forms.Form):
    city = forms.CharField(max_length=30, required=True)
    state = forms.CharField(max_length=30, required=True)
    country = forms.CharField(max_length=30, required=True)
    profile_picture = forms.ImageField(required=True)
    describe_yourself = forms.CharField(required=True, widget=forms.Textarea)
    linked_in_url = forms.URLField(required=True)
    skills = forms.CharField(required=True, widget=forms.Textarea)
    cv = forms.FileField(required=True)


class AddCourseForm(forms.Form):
    thumbnail = forms.ImageField(required=False, validators=[image_file_validator])    
    course_name = forms.CharField(max_length=200)
    description = forms.CharField(required=True, widget=forms.Textarea)
    prerequisite = forms.CharField(required=True, widget=forms.Textarea)
    requirements = forms.CharField(required=True, widget=forms.Textarea)


class Course_ModuleForm(forms.ModelForm):
    class Meta:
        model = Course_Module
        exclude = ('part_of',)

    def clean_video(self):
        ALLOWED_EXTENSIONS = ['.avi']
        video = self.cleaned_data.get('video', False)
        if video:
            ext = os.path.splitext(video.name)[1]

            if (str(ext) in ALLOWED_EXTENSIONS):
                pass
            else:
                raise ValidationError("Please select a Video of type:- ['avi']") 



# Course_ModuleFormSet = forms.inlineformset_factory(Course_Module, form=Course_ModuleForm, extra=1)
Course_ModuleFormSet = forms.modelformset_factory(Course_Module, form=Course_ModuleForm, extra=1, can_order=True, can_delete=True)


class CreatePromoForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'course', 'active']


class ApplyPromoForm(forms.Form):
    promo_code = forms.CharField(max_length=10, required=True, label="Promo Code")