from dotenv import load_dotenv
import os
import requests
from django.shortcuts import render

load_dotenv(override=True)

OAUTH_ENDPOINTS = {
    'google': 'https://accounts.google.com/o/oauth2/v2/auth',
}
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


def index(request):
    template_name = 'core/index.html'
    context = {
        'client_id': CLIENT_ID,
    }
    return render(request, template_name, context)


def get_access_token():
    response = requests.get(url=OAUTH_ENDPOINTS['google'],
                            params={
                                'client_id': CLIENT_ID,
                                'redirect_uri': REDIRECT_URI,
                                'response_type': 'token',
                                'scope': 'profile email',
                            })
    return response.json()