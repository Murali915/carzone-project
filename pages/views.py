from django.shortcuts import render
from .models import team

# Create your views here.

def home(request):
    teams = team.objects.all()
    data = {
        'teams': teams
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
