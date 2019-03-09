from django.shortcuts import render,HttpResponse

def home(request):
    context = {
    'name':'guest',
    }
    return render(request, "home.html", context)
