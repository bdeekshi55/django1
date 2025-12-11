from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("this is about")

# def about(request):
#     return render(request,("about.html"))

def contact(request):
    return HttpResponse("this is contact")

def login(request):
    return render(request,("login.html"))

def home(request):
    return render(request,("home.html"))

