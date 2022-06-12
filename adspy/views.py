from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateNewUser
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .adsapi.fb_ads_library_api_cli import FbAdsApi


def home(request):
    return render(request,'adspy/home page.html ')

#def users(request):
    #return render(request,'adspy/user.html ')

def about(request):
    return render(request,'adspy/about.html ')


#test api  mochkla fil api 
#@login_required(login_url='login')
def users(request):
    args=CreateArgs()
    print(args)
    data=FbAdsApi(args)
    print(data)
    return render(request,'adspy/user.html')


def userlogin(request):
    
    if request.method =='POST':

        usr = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(username=usr,password=pwd)

        if user is not None:
            login(request,user)
            return redirect('user')
        else :
           messages.info(request,'fama mochkla')   
                   
    context = {}
    return render(request,'adspy/login.html',context)


def userlogout(request):
    logout(request)
    return redirect('login')

   



def register(request):
    form = CreateNewUser()
    if request.method =='POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'created Successfully !')
            return redirect('login')
    context = {'form': form}
    return render(request,'adspy/register.html',context)

def CreateArgs():
    t = '-t EAAOmIkyczYcBAGOXPzDv4bgYbbl7cYjY4YW6rZBhPdvARktAlUWyZAz32cuTcZCF4Cybi9Ez5U4FeZB6raVvcJEAMxWC3YmvPLHSeGT45ZCU737heMcBSj7RD8aVMeB8ZCsRXBUmFVQbz0iUv5rJZBd1pd2eOpgPcGZCgfZCfcgwM6hhYBfYxpNDTNCOC4evrYOqMKV1YIHnFzZCkZCOaeTO2TaxRpPJGZBeevDyg9GH3Vih5DKWspEKO03klfjHRPbpEFVnljRaYCHTNgZDZD -f page_id,ad_snapshot_url,ad_delivery_start_time -c CA -s . -v count'
    t=t.split(" ")
    return t
   