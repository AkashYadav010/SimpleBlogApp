from django.shortcuts import render,HttpResponse,redirect
from .models import Blog
from django.contrib.auth import authenticate,login,logout
from blog.forms import AddForm,LoginForm,UpdateForm
from django.views.generic import ListView,DetailView

# def home(request):
#     blog = Blog.objects.all()
#     print(blog)
#     if blog is not None:
#         context = {
#         'blogs':blog,
#         }
#     else:
#         context={
#         'msg':"Sorry No Blogs Yet"
#         }
#     return render(request, "home.html", context)
class HomeView(ListView):
    queryset = Blog.objects.all()
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


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

def detail_view(request, id, *args, **kwargs):
    qs =  Blog.objects.filter(pk=id)
    if qs.exists():
        context = {
        'foundblog':qs.first()
        }
    else:
        return redirect("/")
    return render(request, "detail.html", context)

def update_view(request,id ,*args ,**kwargs):
    qs = Blog.objects.get(pk=id)
    form = UpdateForm(request.POST or None, instance=qs)
    context = {
    'form':form
    }
    if form.is_valid():
        form.save()
        return redirect("/blog/"+str(id))
    return render(request, 'update.html', context)


def delete_view(request, id, *args, **kwargs):
    qs = Blog.objects.get(pk=id)
    context = {
    'foundblog':qs
    }
    if request.method == "POST":
        qs.delete()
        return redirect("home")
    return render(request,'delete.html',context)
