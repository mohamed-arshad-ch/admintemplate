from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']

          user = auth.authenticate(username=username,password=password)

          if user is not None:
              auth.login(request,user)
              return redirect('/home')
          else:
              print("Login Error")
              return redirect('/')

          
     else:
         return render(request,'login.html')
            

         


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print("User Created")
        
        return redirect('/')


    else:

        return render(request,'register.html')



def home(request):
    return render(request,'home.html')



def logout(request):
    auth.logout(request)
    return redirect('/')