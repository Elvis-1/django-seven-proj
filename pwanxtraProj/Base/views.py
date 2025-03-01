from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail,BadHeaderError
from smtplib import SMTPException 

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def soldout(request):
    return render(request, 'soldout.html')

def contact(request):
    # send email
   
#   <!-- name,phone,email,subject,message -->
    if request.method == 'POST':
       print('This is called ooooooooooooooo')
       name = request.POST.get('name').strip()
       phone = request.POST.get('phone').strip()
       email = request.POST.get('email').strip()
       subject = request.POST.get('subject').strip()
       message = request.POST.get('message').strip()
       
       my_email = 'info@pwanxtra.com'
       try:
           validate_email(email)
       except ValidationError:
           email = None
       if not phone.isdigit():
           phone  = None
           messages.error('Invalid phone number')
           return redirect('contact')
        
           
       if name and phone and email:
           email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"

           try:
               send_mail(
                   subject= subject,
                   message= email_message,
                   from_email = my_email,
                   recipient_list= [my_email],
               )
               messages.success(request,'Mail sent  successfully')
               return redirect('contact')

           except BadHeaderError:
                messages.error(request, "Invalid email header found.")
           except SMTPException as e:
                messages.error(request, f"SMTP error: {str(e)}")
           except Exception as e:
                messages.error(request, f"Unexpected error: {str(e)}") 

       else:
          messages.error(request,'Please fill all the required fields')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

# estates

def akaEzePhase2(request):
    return render(request, 'AkaEze Phase 2.html')

def isuraPhase2(request):
    return render(request, 'isura.html')

def ngozi(request):
    return render(request, 'ngozi.html')

def ikenga(request):
    return render(request, 'ikenga.html')

def nkem(request):
    return render(request, 'nkem.html')

def Aku(request):
    return render(request, 'Aku.html')

def ileri(request):
    return render(request, 'ileri.html')

def IleAyo3(request):
    return render(request, 'ile Ayo 3.html')

def Enyiaba2(request):
    return render(request, 'Enyiaba2.html')

# estates ends




