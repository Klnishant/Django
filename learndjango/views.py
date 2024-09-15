from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutPage(request):
    return HttpResponse("This is the aboutpage of this website")

def contactPage(request):
    return HttpResponse("This is the contactpage of this website")