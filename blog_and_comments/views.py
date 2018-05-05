from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from registration.models import *
from django.forms.models import model_to_dict
from django.contrib import messages
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User



def list_blogs(request):
    blog_list = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_list, 2)  #Change the number of blogs you want to see per page here
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blogs.html', { 'blogs': blogs })

def view_blog(request, id=None):
    blog = get_object_or_404(Blog, id=id)
    context = {"blog":blog}
    return render(request, "view_blog.html", context)



@login_required(login_url='/authentication/login/', redirect_field_name='next')
def create_blog(request):
    user = request.user
    custom_user = get_object_or_404(Custom_User, user=user)
    if request.method == "POST":
        print request.POST
        form = CreateBlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            print "\n" * 10
            print "is valid"
            instance = form
            title = instance.cleaned_data.get('title')
            image = instance.cleaned_data.get('image')
            content = instance.cleaned_data.get('content')
            draft = instance.cleaned_data.get('draft')
            blogger = custom_user
            blog = Blog.objects.create(
                title = title,
                image = image,
                content = content,
                draft = draft,
                blogger = blogger
            )
            blog.save()
            return HttpResponseRedirect(blog.get_absolute_url())
        context = {"form":form}
    else:
        form = CreateBlogForm()
        context = {"form":form}
    return render(request, "create_blog.html", context)


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def update_blog(request, id=None):
    user = request.user
    custom_user = get_object_or_404(Custom_User, user=user)
    blog = get_object_or_404(Blog, id=id)
    if blog.blogger != custom_user:
        return HttpResponseRedirect("not_your_blog")
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form
            print "\n" * 10
            print blog.image
            print instance.cleaned_data.get('image')
            if (blog.image == "" and instance.cleaned_data.get('image') == None):
                print "IF"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = blog.image
            elif (blog.image != "" and instance.cleaned_data.get('image') == None):
                print "ELIF"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = blog.image
            elif (blog.image != "" and instance.cleaned_data.get('image') != None):
                print "2nd ELIF"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = instance.cleaned_data.get('image')
            elif (blog.image == "" and instance.cleaned_data.get('image') != None):
                print "3rd ELIF"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = instance.cleaned_data.get('image')
            elif (blog.image == False):
                print "4th ELIF"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = ""
            else:
                print "ELSE"
                print blog.image
                print instance.cleaned_data.get('image')
                blog.image = blog.image
            blog.title = instance.cleaned_data.get('title')
            blog.content = instance.cleaned_data.get('content')
            blog.draft = instance.cleaned_data.get('draft')
            blog.save()
            return HttpResponseRedirect(blog.get_absolute_url())
        context = {"form":form}
    else:
        form = CreateBlogForm(initial=model_to_dict(blog))
        context = {"form":form}
    return render(request, "update_blog.html", context)


@login_required(login_url='/authentication/login/', redirect_field_name='next')
def delete_blog(request, id=None):
    user = request.user
    custom_user = get_object_or_404(Custom_User, user=user)
    blog = get_object_or_404(Blog, id=id)
    if blog.blogger != custom_user:
        return HttpResponseRedirect("not_your_blog")
    blog.delete()
    messages.success(request, "Successfully Deleted.")
    return redirect("list_blogs")
    

@login_required(login_url='/authentication/login/', redirect_field_name='next')
def blog_like_toggle(request, id=None):
    obj = get_object_or_404(Blog, id=id)
    user = request.user
    if user.is_authenticated():
        custom_user = get_object_or_404(Custom_User, user=user)
        if custom_user.id: 
            if custom_user in obj.likes.all():
                obj.likes.remove(custom_user)
            else:
                obj.likes.add(custom_user)
    return HttpResponseRedirect(obj.get_absolute_url())



class BlogLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):
        # id = self.kwargs.get("id")
        obj = get_object_or_404(Blog, id=id)
        user = self.request.user
        updated = False
        liked = False
        
        if user.is_authenticated():
            custom_user = get_object_or_404(Custom_User, user=user)
            if custom_user.id: 
                if custom_user in obj.likes.all():
                    obj.likes.remove(custom_user)
                    liked = False                    
                else:
                    obj.likes.add(custom_user)
                    liked = True
                updated = True
        data = {
            "updated": updated,
            "liked": liked
        }    
        return Response(data)