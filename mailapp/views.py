from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Test',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['prazzwalthapa87@gmail.com',],
                  fail_silently = False
                    )
    return render(request, 'home.html', {})
