from django.shortcuts import render,HttpResponse,redirect
from .models import Blog
from django.contrib.auth import authenticate,login,logout
from blog.forms import AddForm,LoginForm

def home(request):
    blog = Blog.objects.all()
    if blog is not None:
        context = {
        'blogs':blog,
        }
    else:
        context={
        'msg':"Sorry No Blogs Yet"
        }
    return render(request, "home.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
    'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user     = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,"login_page.html", context)


def add_blog(request):
    add_form = AddForm(request.POST or None)
    context = {
    'form':add_form
    }
    if add_form.is_valid():
        new_blog = Blog()
        new_blog.title = add_form.cleaned_data.get('title')
        new_blog.content = add_form.cleaned_data.get('content')
        new_blog.author = request.user
        new_blog.save()
        return redirect("/")
    return render(request, "addform.html", context)
