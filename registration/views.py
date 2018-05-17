from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core import signing
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages 
from django import forms
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def custom_user_creation(request):
    current_site = str(get_current_site(request))
    form = CommonRegistrationForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        instance = form
        first_name = instance.cleaned_data.get("first_name")
        last_name = instance.cleaned_data.get("last_name")
        mobile = instance.cleaned_data.get("mobile")
        email = instance.cleaned_data.get("email")
        password = instance.cleaned_data.get("password")
        register_as = instance.cleaned_data.get("register_as")
        u, created = User.objects.get_or_create(email=email)
        if created == False:
            if u.is_active:
                return HttpResponseRedirect('/already_registered')
            else:
                return HttpResponseRedirect('/activation_pending')
        else:
            # Save User Model
            u.is_active = False
            u.is_staff = False
            u.is_superuser = False
            u.first_name = first_name
            u.last_name = last_name
            u.set_password(password)
            u.username = email
            u.save()
            # Save the Custom User Model
            custom_user = Custom_User.objects.create(user=u, mobile=mobile, primary_registration_type=register_as)
            custom_user.save()                        
            print "\n"*20
            print custom_user.primary_registration_type
            print "\n"*20
            print type(custom_user.primary_registration_type) 
            if str(custom_user.primary_registration_type) == "Trainer":
                new_trainer = Trainer_Model.objects.create(user=custom_user)
                new_trainer.save()          
            # Encrypt Activation Link
            salt = settings.SECRET_KEY
            ak = signing.dumps(u.email, salt)
            # Send Activation Link to the newly registered user
            # send_mail('Click the link below to activate yor Account for ' + current_site, 
            # "http://" + current_site +'/authentication/activate_trainer/?ak=' + ak, 
            # settings.EMAIL_HOST_USER,
            # [u.email], 
            # fail_silently=False)
            send_mail('Click the link below to activate yor Account for ' + "localhost:8080", 
            "http://" + "localhost:8080" +'/authentication/activate_user/?ak=' + ak, 
            settings.EMAIL_HOST_USER,
            [u.email], 
            fail_silently=False)
            return HttpResponseRedirect('/authentication/activation_mail_sent')
        context = {"form": form}
    return render(request, "user_creation.html", context)


def activate_user(request):
    print "\n"*20
    print "Activating...."
    salt = settings.SECRET_KEY
    ak = request.GET.get('ak')
    # Change below line max_age according to your settings.py file
    decrypt = signing.loads(ak, salt)
    print "\n" * 20
    print decrypt
    u = User.objects.get(email=decrypt)
    print "\n" * 20    
    print type(u)
    try:
        print "Inside Try"
        print u
        if u.is_active == False:       
            print "Inside Try > IF" 
            u.is_active = True
            print "User set to active"
            u.save()
            print "User Saved"
            return HttpResponseRedirect('/accounts/activate/complete/')
            # return render(request, "activation_successful.html", {})
            print "after return"
        else:
            print "Inside Else"
            return HttpResponseRedirect('/authentication/activated_already')
            # return render(request, "already_activated.html", {})
            print "after else return"
    except:
        print "Inside except"
        return render(request, "activation_failed.html", {})


def my_login(request):
    try:
        next = request.GET.get('next')
        if next:
            print next
        else:
            print "no next" 
    except Exception as e:
        print e
    form = LoginForm(request.POST or None)
    context ={"form":form}
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        print email
        print password
        try:
            user = User.objects.get(email=email) 
            username = user.username
            print user
            user = authenticate(username=username, password=password)
            print user
        except:
            raise forms.ValidationError("User not found")
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    custom_user = Custom_User.objects.get(user = user)
                except:
                    return HttpResponseRedirect("/")
                if custom_user is not None:
                    if str(custom_user.primary_registration_type) == "Trainer":
                        print "Login as a Trainer."
                        if next:
                            return HttpResponseRedirect(next) 
                        return HttpResponseRedirect("/trainer_dashboard/")
                    if str(custom_user.primary_registration_type) == "Learner":
                        print "Login as a Learner." 
                        return HttpResponseRedirect("/learner_dashboard/")
                    if str(custom_user.primary_registration_type) == "Vendor":
                        print "Login as a Vendor." 
                        if next:
                            return HttpResponseRedirect(next)
                        return HttpResponseRedirect("/vendor_dashboard/")
                    if str(custom_user.primary_registration_type) == "Job Seeker":
                        print "Login as a Job Seeker." 
                        if next:
                            return HttpResponseRedirect(next)
                        return HttpResponseRedirect("/job_seeker_dashboard/")
                    if str(custom_user.primary_registration_type) == "Client":
                        print "Login as a Client." 
                        if next:
                            return HttpResponseRedirect(next)
                        return HttpResponseRedirect("/client_dashboard/")
            else:
                return HttpResponseRedirect("/activation_pending/")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Incorrect Password.')
            context ={"form":form}      
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def trainer_update_profile(request):
    user = request.user
    if user.is_active == False:
        return HttpResponseRedirect('/activation_pending/')
    print user
    cu = Custom_User.objects.get(user=user)
    print cu
    print cu.primary_registration_type
    if cu.primary_registration_type == "Trainer":
        print "True"
        trainer = Trainer_Model.objects.get(user=cu)
        print trainer
        form = UpdateTrainerProfileForm(request.POST, request.FILES or None)
        context = {"form": form}
        if form.is_valid():
            instance = form
            city = instance.cleaned_data.get('city')
            state = instance.cleaned_data.get('state')
            country = instance.cleaned_data.get('country')
            profile_picture = instance.cleaned_data.get('profile_picture')
            describe_yourself = instance.cleaned_data.get('describe_yourself')
            linked_in_url = instance.cleaned_data.get('linked_in_url')
            skills = instance.cleaned_data.get('skills')
            cv = instance.cleaned_data.get('cv')

            trainer.city = city
            trainer.state = state
            trainer.country = country
            trainer.profile_picture = profile_picture
            trainer.describe_yourself = describe_yourself
            trainer.linked_in_url = linked_in_url
            trainer.skills = skills
            trainer.cv = cv
            trainer.save()
            return HttpResponseRedirect("/trainer_profile_updated/")            
        else:
            messages.error(request, 'Something went wrong.')
            form = UpdateTrainerProfileForm(request.POST, request.FILES or None)
            context = {"form": form}
    else:
        return HttpResponseRedirect("/not_a_trainer/")
    return render(request, "trainer_update_profile.html", context)


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def display_courses(request):
    user = request.user
    cu = get_object_or_404(Custom_User, user=user)
    trainer = get_object_or_404(Trainer_Model, user=cu)
    if cu.primary_registration_type == 'Trainer' and trainer:    
        trainer_courses = Course.objects.all().filter(course_by=trainer)
        return render(request, "display_courses.html", {"trainer_courses":trainer_courses})
    else:
        return HttpResponseRedirect("/invalid_trainer")


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def add_course(request):
    user = request.user
    cu = get_object_or_404(Custom_User, user=user)
    trainer = get_object_or_404(Trainer_Model, user=cu)
    if cu.primary_registration_type == 'Trainer' and trainer:
        if request.method == 'POST':
            form = AddCourseForm(request.POST, request.FILES or None)
            context = {"form": form}
            if form.is_valid():
                instance = form
                thumbnail = instance.cleaned_data.get('thumbnail')
                course_name = instance.cleaned_data.get('course_name')
                description = instance.cleaned_data.get('description')
                prerequisite = instance.cleaned_data.get('prerequisite')
                requirements = instance.cleaned_data.get('requirements')
                course_by = trainer

                new_course = Course.objects.create(
                    course_by = course_by,
                    thumbnail = thumbnail,
                    course_name = course_name,
                    description = description,
                    prerequisite = prerequisite,
                    requirements = requirements
                )
                return HttpResponseRedirect("/trainer_profile_updated/")            
            else:
                messages.error(request, 'Something went wrong.')
                form = AddCourseForm(request.POST, request.FILES or None)
                context = {"form": form}
        else:
            form = AddCourseForm(request.POST, request.FILES or None)
            context = {"form": form}
    else:
        form = AddCourseForm(request.POST, request.FILES or None)
        return HttpResponseRedirect("/invalid_trainer/")
    return render(request, "add_course.html", context)


def test_view(request):
    c = Course.objects.get(id=1)
    trainer = c.course_by 
    custom_user = trainer.user
    regular_user = custom_user.user
    full_name = regular_user.get_full_name
    context = {
        "c":c,
        "trainer": trainer,
        "custom_user": custom_user,
        "regular_user": regular_user,
        "full_name": full_name
        }
    return render(request, "test.html", context)


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def edit_course_details(request, course_id=None):
    user = request.user
    custom_user = get_object_or_404(Custom_User, user=user)
    if custom_user.primary_registration_type == "Trainer":
        trainer = get_object_or_404(Trainer_Model, user=custom_user)
        course = get_object_or_404(Course, id=course_id)
        if course.course_by == trainer:
            if request.method == 'POST':
                form = AddCourseForm(request.POST, request.FILES or None)
                instance = form
                if form.is_valid():
                    instance = form
                    if (course.thumbnail == "" and instance.cleaned_data.get('thumbnail') == None):
                        course.thumbnail = course.thumbnail
                    elif (course.thumbnail != "" and instance.cleaned_data.get('thumbnail') == None):
                        course.thumbnail = course.thumbnail
                    elif (course.thumbnail != "" and instance.cleaned_data.get('thumbnail') != None):
                        course.thumbnail = instance.cleaned_data.get('thumbnail')
                    elif (course.thumbnail == "" and instance.cleaned_data.get('thumbnail') != None):
                        course.thumbnail = instance.cleaned_data.get('thumbnail')
                    elif (course.thumbnail == False):
                        course.thumbnail = ""
                    else:
                        course.thumbnail = course.thumbnail
                    course.course_name = instance.cleaned_data.get('course_name')
                    course.description = instance.cleaned_data.get('description')
                    course.prerequisite = instance.cleaned_data.get('prerequisite')
                    course.requirements = instance.cleaned_data.get('requirements')
                    course.course_by = trainer 
                    course.save()
                    return HttpResponseRedirect("course_details_updated_successfully")
                context = {"text": "edit", "form":form}
            else:
                form = AddCourseForm(initial=model_to_dict(course))
                context = {"text": "edit", "form":form}            
        else:
            context = {"text": "Not authorised to edit"}
    else:
        context = {"text": "You are not a trianer."}
    return render(request, "edit_course.html", context)


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def edit_course_modules(request, course_id=None, *args, **kwargs):
    user = request.user
    cu = Custom_User.objects.get(user=user)
    trainer = Trainer_Model.objects.get(user=cu)
    if cu.primary_registration_type == 'Trainer':    
        course = Course.objects.get(course_by=trainer, id=course_id)
        queryset = course.modules.all()
        return render(request, "edit_modules.html", {"course": course, "queryset": queryset})
    else:
        return HttpResponseRedirect('/invalid_trainer/')



def browse_courses(request):
    context = {}
    return render(request, "browse_courses.html", context)