from django.shortcuts import render, redirect
from django.core.mail import send_mail
from accounts.models import Token
from django.core.urlresolvers import reverse
SUCCESS_MESSAGE = "Check your email, we've send you a link you can use to log in."
from django.contrib import auth, messages


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    # print(type(send_mail))
    # send_mail(
    #     'Your login link for Superlists',
    #     'body text tbc',
    #     'noreply@superlists',
    # [email],
    # )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )
    
    messages.success(
        request,
        SUCCESS_MESSAGE
    )

    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
