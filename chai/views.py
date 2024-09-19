from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import ChaiVariety,Stores
from .forms import chaiVarietyForms

# Create your views here.
def chaiPage(request):
    chais = ChaiVariety.objects.all()
    return render(request,'chai.html',{'chais':chais})

def chaiDetails(request,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,'chaiDetails.html',{'chai':chai})

def chai_store_view(request):
    stores = None

    if request.method == 'POST':
        form = chaiVarietyForms(request.POST)

        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Stores.objects.filter(chai_variety=chai_variety)

    else:
        form = chaiVarietyForms()

    return render(request,'chaiStores.html',{'form':form,'stores':stores})