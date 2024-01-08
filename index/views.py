from django.shortcuts import render, redirect


# Create your views here.
def index(request):

    return render(request,'index/index.html')

def temp(request):
    return render(request,'index/temp.html')