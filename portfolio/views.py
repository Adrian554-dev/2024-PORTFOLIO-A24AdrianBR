from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    # return HttpResponse("Hellow there friend")
    projects=Project.objects.all()
    return render(request, 'generator/home.html',{'projects':projects})


