from django.shortcuts import render,HttpResponse
from django.contrib import messages
# Create your views here.
#   <!-- name,phone,email,subject,message -->

from django.core.mail import send_mail,BadHeaderError
from smtplib import SMTPException 





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message')

        if name and email and message:
            email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"

            try:
                
                send_mail(
                    subject,
                    email_message,
                    'info@pwanxtra.com',  # Must match EMAIL_HOST_USER in settings
                    ['info@pwanxtra.com','Jeremy@buzydev.com'],  # Change to the recipient email
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
                return render(request, 'contact.html')

            except BadHeaderError:
                messages.error(request, "Invalid email header found.")
            except SMTPException as e:
                messages.error(request, f"SMTP error: {str(e)}")
            except Exception as e:
                messages.error(request, f"Unexpected error: {str(e)}")

        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contact.html')


