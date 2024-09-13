from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import My_User


# Create your views here.
def home(request):
    return render(request,'base/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()

        my_user_data = My_User(username=username,
                               name=str(fname)+' '+str(lname),
                               email=email)
        my_user_data.save()
        
        messages.success(request,'Signed Up Successfully')
        
        return redirect('signin')
        
    
    return render(request,'base/signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            fname= user.first_name
            return render(request,'base/index.html',{'fname':fname})
        else:
            messages.error(request,'Please Login First')
            redirect('home')
    
    return render(request,'base/signin.html')
def signout(request):
    logout(request)
    messages.success(request,'successfully logouted')
    return redirect('home')


