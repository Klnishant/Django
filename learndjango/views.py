from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutPage(request):
    return render(request,"about.html")
def contactPage(request):
    return render(request,"contact.html")