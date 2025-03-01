from django . shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from todoapp.models import TODOO
from django.contrib.auth import authenticate,login as auth_login,logout

from django.db import IntegrityError


def signup(request):
    # you you@you.com 1234
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailId = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm,emailId,pwd)

        if User.objects.filter(email= emailId).exists():
            return render(request,'signup.html',{'error':'Email already exists'})
        try:
           my_user = User.objects.create_user(username=fnm, email= emailId,password= pwd)
           my_user.save()
        except IntegrityError: return render(request, 'signup.html', {'error': "User name exists"})
      
        return redirect('/login')
   
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('fnm')  # This field seems to represent the email in your signup form
        pwd = request.POST.get('pwd')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=pwd)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('/todopage')
        else:
            return render(request, 'login.html', {'error': "Invalid email or password"})
    return render(request, 'login.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('fnm')
#         pwd = request.POST.get('pwd')
        
#         print("Received:", email, "Password:", pwd)  # Debugging
#         print("Request POST Data:", request.POST) 
#         print(email,'password:',pwd)
#         user = authenticate(request,username=email,password =pwd)
#         print("Authenticated User:", user)

#         if user is not None:
#             auth_login(request,user)
#             return redirect('/todopage')
#         else:
#             return render(request,'login.html', {'error':"User does not exist"})
#             # return redirect('/login')
#     return render(request,'login.html')

@login_required(login_url='/login')  
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print('This is the title')
        obj = TODOO(title=title, user= request.user)
        obj.save()

        res = TODOO.objects.filter(user = request.user).order_by('-date')
        return redirect('/todopage',)
    res = TODOO.objects.filter(user = request.user).order_by('-date')

    return render(request,'todo.html', 
                  {'res':res,}
                  )
@login_required(login_url='/login') 
def edit_todo(request, srno):
    obj = TODOO.objects.get(srno = srno)
    if request.method == 'POST':
        title = request.POST.get('title')
        print('This is the title '+ title)
        obj = TODOO.objects.get(srno = srno)
        obj.title = title
        obj.save()

        res = TODOO.objects.filter(user = request.user).order_by('-date')
        return redirect('/todopage',)
    res = TODOO.objects.filter(user = request.user).order_by('-date')
   
    print('This is the title ' + obj.title)  # Add this line before rendering the template
    return render(request,'edit_todo.html', 
                  {'obj':obj})
    
@login_required(login_url='/login') 
def delete_todo(request, srno):
    obj = TODOO.objects.get(srno = srno)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/login')
 