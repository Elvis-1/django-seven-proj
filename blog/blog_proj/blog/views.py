from django.shortcuts import render,redirect
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse


# username:blog
# email: blog@blog.com
# pass: 1234
# Create your views here.

def test(request):
    return render(request,'blog/base.html')

def login(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password') 
       
       try:
         userObj = User.objects.get(email=email)

         userr = authenticate(request,username=userObj.username,password=password) 

       except User.DoesNotExist:
           messages.error(request,'User does not exist' )
           return render(request,'blog/login.html')
       
       if userr is not None:
           auth_login(request,userr)
           return redirect(reverse('home'))
       else:
           print("Authentication failed!") 
           messages.success(request,'Login successfully')
           return redirect('/loginn')
    return render(request,'blog/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        print('this is email '+ email)
        if User.objects.filter(email=email).exists():
            return render(request,'blog/signup.html', {'error':'Email already exists'})
        try:
           newUser = User.objects.create_user(username=name,email=email,password=password)
           newUser.save()
        except IntegrityError:
            return render(request,'blog/signup.html', {'error':'User name already exists'})
        
        return redirect('/loginn')
    return render(request,'blog/signup.html')

@login_required(login_url=reverse_lazy('login'))
def home(request):
    context = {
        'posts':Posts.objects.all().order_by('-date_posted')
    }
    return render(request,'blog/home.html',context)

def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = Posts(title=title,content=content,author=request.user)
        npost.save()
        return redirect(reverse('home'))
    return render(request, 'blog/newpost.html')


@login_required(login_url=reverse_lazy('login')) # the name defined in my url
def myPost(request):
    context =  {'posts': Posts.objects.filter(author= request.user)}
    return render(request,'blog/mypost.html',context)

def signout(request):
    logout(request)
    return redirect(reverse('login'))
