from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

#login 
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
              #return render(request,'login.html')
              raise Http404("No user matches the given query.")
          
     else:
         return render(request,'login.html',{'message':"Invalid"})
            

         
#register 

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


#home Page
@login_required(login_url='/')
def home(request):
    if request.method == 'POST':
        username = request.POST['q']
        me = User.objects.get(username=username)
        print(me)
        return render(request,'search.html',{'mee':me})
    else:
     
          me = User.objects.all()
          return render(request,'home.html',{'dat':me})
   


#logout
def logout(request):
    auth.logout(request)
    return redirect('/')

def delete(request , id):
    try:
        u = User.objects.get(id=id)
        u.delete()
        print('deleted')
        return redirect('/home')
    except:
         raise Http404("No user matches the given query.")
    

def edit(request , id):
    try:
        
        us =  User.objects.get(id=id)
        
        return render(request,'edit.html',{'use':us})
    except:
        print("error")
   

def update(request , id):
    try:
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        
        mee = User.objects.get(id = id)
        mee.username = username
        mee.first_name = first_name
        mee.email = email
        mee.save()
        return redirect('/home')

    except :
        print('error')


def search(request):
    pass    
              


    