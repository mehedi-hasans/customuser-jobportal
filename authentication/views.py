from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentication.forms import SignupForm
from django.contrib import messages

from authentication.models import CustomUser
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Creation Successfully")
            return redirect('login')
        else:
            messages.warning(request,'Invalid Information')
            return redirect('signup')
    else:
        form= SignupForm()
    return render(request, 'signup.html', {'form': form})
 

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def profile(request):

    return render(request, 'profile.html')

def profileEdit(request):
    # user = CustomUser.objects.get(id = user.id)
    # customUser = User.CustomUser.objects.get(id = user.id)

    return render(request, 'profile/editProfile.html')