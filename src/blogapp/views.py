from django.shortcuts import render,HttpResponse
from .models import Blog

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
