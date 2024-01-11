from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm,SignInForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def signup_f(request):
    
    if request.method=="POST":
        form=UserForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserForm()
            

    return render(request,'signup.html',{'form':form})

def SignIn(request):   
    if request.method=="POST":
        form=SignInForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.warning(request,'The User Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user:
                
                login(request, user)
                return redirect("home")
    else:
        form=SignInForm()
    return render(request,'login.html',{'form':form})

def home(request):
    return render(request,"home.html")

def logout_f(request):
    logout(request)
    return redirect('login')
