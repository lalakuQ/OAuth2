from dotenv import load_dotenv
import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth import authenticate, login
import uuid
from .backends import GoogleAuthBackend
from django.contrib import messages
from django.contrib.auth import get_user_model
load_dotenv(override=True)

def get_state():
    return str()

OAUTH_ENDPOINTS = {
    "init_url": "https://accounts.google.com/o/oauth2/v2/auth",
    "token_url": "https://oauth2.googleapis.com/token",
    "info_url": "https://www.googleapis.com/oauth2/v3/userinfo",
}

GOOGLE_CLIENT_ID = os.getenv('CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.getenv('REDIRECT_URI')
GOOGLE_LOGIN_REDIRECT_URI = (f'https://accounts.google.com/o/oauth2/v2/auth?'
                             f'client_id={GOOGLE_CLIENT_ID}&'
                             f'redirect_uri=http://localhost:8000/google/callback&'
                             f'response_type=code&'
                             f'scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile&'
                             f'access_type=offline')


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def google_login(request):

    return HttpResponseRedirect(GOOGLE_LOGIN_REDIRECT_URI)

User = get_user_model()
def google_callback(request):
    if 'code' in request.GET:
        user = authenticate(request, code=request.GET.get('code'), backend=GoogleAuthBackend)
        if user:
            login(request, user=user)
        else:
            print(request, "You are not Authorized to Login ")
        return redirect('core:index')
    else:
        return render(request, template_name='core/index.html')
