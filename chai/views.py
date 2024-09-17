from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import ChaiVariety

# Create your views here.
def chaiPage(request):
    chais = ChaiVariety.objects.all()
    return render(request,'chai.html',{'chais':chais})

def chaiDetails(request,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,'chaiDetails.html',{'chai':chai})