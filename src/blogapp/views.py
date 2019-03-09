from django.shortcuts import render,HttpResponse,redirect
from .models import Blog
from blog.forms import AddForm

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



def add_blog(request):
    add_form = AddForm(request.POST or None)
    context = {
    'form':add_form
    }
    if add_form.is_valid():
        new_blog = Blog()
        print(add_form.cleaned_data)
        new_blog.title = add_form.cleaned_data.get('title')
        new_blog.content = add_form.cleaned_data.get('content')
        new_blog.author = request.user
        new_blog.save()
        return redirect("/")
    return render(request, "addform.html", context)
