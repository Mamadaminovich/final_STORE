from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_email(email, token):
    subject = 'Reset Password'
    message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/reset_password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    
    return True