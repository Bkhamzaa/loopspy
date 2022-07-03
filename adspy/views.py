from contextlib import ContextDecorator
from email import parser
from multiprocessing import context
from tkinter import Y
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
from .adsapi.fb_ads_library_api_cli import FbAdsApi,get_parser
from bs4 import BeautifulSoup, Script
import time
from selenium import webdriver
import  copy
import re
import urllib.request
import json




def home(request):
    return render(request,'adspy/home page.html ')

#def users(request):
    #return render(request,'adspy/user.html ')

def about(request):
    return render(request,'adspy/about.html')


#test api  mochkla fil api 
#@login_required(login_url='login')
def users(request):
    args=CreateArgs()
    data=FbAdsApi(args)
    errormsg={}
    GetOk=False
    
    context={}
    try :
        context=data
    except:  
        context=data
    new_data=[]
    #next_page=data["paging"]["next"]
    new_data=copy.deepcopy(data["data"])
    ty= []
    for i in range(3):
        
        page=get_data_from_page(new_data[i]["ad_snapshot_url"])
        
        y=(new_data[i]|page) 
        ty.append(y)
        #ty= ty|y

    #print(y["cards"][1]['original_image_url'])
    #print(ty[0]['cards'][0]['original_image_url'])
    print(ty[-1])
    vid=ty[-1]['videos'][0]['video_hd_url']
    #print(img)
    
    return render(request,'adspy/user.html',{"vid":vid})


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
    token="EAAOmIkyczYcBAHjADh0DeTjrZCGs8zzJMITcTnZCbGjKgkoQ8ctyfYKEW55ejZB6KwUYcFgibiRcjchcKg0KDj5xHVJmh6JPwWpqyhYcfZCZBWV0aIGMYsCnALovplQ3tvRItP0CrHHO9fFvvxkrwQYggZC4jLucDWUf8MC5x3aXfInUtXrZCev0FIA2JGjsiqUfXhqeIvM0GH0byRzM6D54XZCJ0GkWTxLXMx61ZBGPqqxSvZBewIzPG5cllE9letW0Ja8prSDQgAfgZDZD"
    t = '-t '+token+' -f page_id,ad_snapshot_url,ad_creative_link_titles,ad_creative_link_descriptions,ad_delivery_start_time -c CA -s . -v count,'
    t=t.split(" ")
    return t
   









def get_data_from_page(url):
    fp = urllib.request.urlopen(url)

    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()


    found =re.search('"snapshot"(.+),"spend"', mystr)
    link_img=mystr[found.start():found.end()]

    list_str=link_img.replace(',"spend"','')
    list_str=list_str.replace('"snapshot":','') 


    data = json.loads(list_str)
    #print(mystr)
    cards=data.get('cards')
    img=data.get('images')
    vid=data.get('videos')
    pic_profile_fb=data.get('page_profile_picture_url')
    pic_profile_instagme=data.get('instagram_profile_pic_url')
    cta_type=data.get('cta_type')

    data_page={}
    data_page["cards"]=copy.deepcopy(cards)
    data_page["images"]=copy.deepcopy(img)
    data_page["videos"]=copy.deepcopy(vid)
    data_page["page_profile_picture_url"]=copy.deepcopy(pic_profile_fb)
    data_page["instagram_profile_pic_url"]=copy.deepcopy(pic_profile_instagme)
    data_page["cta_type"]=copy.deepcopy(cta_type)
    return data_page