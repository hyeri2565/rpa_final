from django.shortcuts import render
from .models import Content
import pyautogui
def start(request):
    allContents=Content.objects.all()
    context={
        'allContents':allContents
    }
    return render(request,'start.html',context)
def step1(request):
    return render(request,'index0.html')
def step2(request):
    return render(request,'index.html')
def contents(request):
    #allContents=Content.objects.filter(Order="contentorder")
    #ordervalue=request.POST["contentorder"]
    ordervalue=request.POST.get("contentorder")
    contentvalue=Content.objects.filter(Order = ordervalue)

    context={
        #'allContents':allContents,
        #'orderkey':ordervalue,
        'ordervalue':ordervalue,
        'contentvalue':contentvalue

        }
    return render(request,'contents_index.html', context)

def contents2(request):
    content_all=Content.objects.all()
    context={
        'content_all':content_all
    }
    return render(request,'contents_index2.html',context)

def move(x,y):
    return pyautogui.moveTo(x,y)
# Create your views here.
