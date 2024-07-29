from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from dotenv import load_dotenv
import os
import json
from django.contrib.auth import get_user_model
import requests
from django.shortcuts import render
load_dotenv(override=True)

OAUTH_ENDPOINTS = {
    "init_url": "https://accounts.google.com/o/oauth2/v2/auth",
    "token_url": "https://oauth2.googleapis.com/token",
    "info_url": "https://www.googleapis.com/oauth2/v3/userinfo",
}
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

User = get_user_model()
class GoogleAuthBackend(BaseBackend):
    def _get_access_token(self, code=None):
        response = requests.post(url=OAUTH_ENDPOINTS['token_url'],
                                 data={
                                    'code': code,
                                    'client_id': CLIENT_ID,
                                    'client_secret': CLIENT_SECRET,
                                    'redirect_uri': 'http://localhost:8000/google/callback',
                                    'grant_type': 'authorization_code'
                                })
        access_token = json.loads(response.content)['access_token']
        return access_token


    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, code=None, **kwargs):
        if code:
            access_token = self._get_access_token(code=code)
            if access_token:
                
                google_user_details = requests.get(f'{OAUTH_ENDPOINTS['info_url']}?access_token={access_token}')
                user, created = User.objects.get_or_create(username=google_user_details.json().get('email'))
                return user
