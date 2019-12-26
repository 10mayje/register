from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib import  messages
from django.contrib.auth.decorators import login_required
posts=[
    {
        'author':'tanmay',
        'tittle':'test',
        'work':'web',

    },
    {
        'author': 'tanmayto',
        'tittle': 'test2',
        'work': 'web2',

    }

]

# Create your views here
def home(request):
    context={
        'posts':posts
    }
    return render(request,"account/index.html",context)
def new(request):
    return render(request,"account/html.html")



def register(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"account/index.html")
    else:
        form=UserCreationForm()

    return render(request,'account/test.html',{'form':form})
@login_required()
def profile(request):
    return render(request,'account/profile.html')
