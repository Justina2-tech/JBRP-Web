import random
import string
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

class EmailUtils:
    @staticmethod
    def send_mail_service(to_email, subject, message):
        send_mail(subject, message, 'learning.thbs@gmail.com', [to_email], fail_silently=False)

    @staticmethod
    def send_otp_service(to_email):
        otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        EmailUtils.send_mail_service(to_email, 'Your OTP is', f'Your OTP is: {otp}')
        return otp

    @staticmethod
    def send_new_password_service(to_email, new_password):
        EmailUtils.send_mail_service(to_email, 'Your New Password', f'Your new password is: {new_password}')
