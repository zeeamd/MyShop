from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
            fn = request.POST['first_name']
            ln = request.POST['last_name']
            un = request.POST['username']
            pw1 = request.POST['password1']
            pw2 = request.POST['password2']
            if pw1 == pw2:
                if User.objects.filter(username=un).exists():
                    messages.info(request,'user already exists')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=un,password=pw1,first_name=fn,last_name=ln)
                    user.save()
                    return redirect("/retail")
            else:
                messages.info(request,'password did not match')
                return redirect('/register')
    else:
        return render(request,'register.html')
            
def login(request):
    if request.method=='POST':
        un = request.POST['username']
        pw = request.POST['password']  
        user = auth.authenticate(username=un,password=pw) 
        if user is not None:
            auth.login(request, user)
            return redirect('/retail')
        else:
            messages.info(request,'username or password incorrect')
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
        
def landingPage(request):
    return render(request,'landingpage.html')
