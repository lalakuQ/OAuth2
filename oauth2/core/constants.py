import os

from dotenv import load_dotenv

load_dotenv(override=True)


GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

GOOGLE_OAUTH_ENDPOINTS = {
    'init_url': 'https://accounts.google.com/o/oauth2/v2/auth',
    'token_url': 'https://oauth2.googleapis.com/token',
    'info_url': 'https://www.googleapis.com/oauth2/v3/userinfo',
}
GOOGLE_REDIRECT_URI = 'http://localhost:8000/google/callback'
GOOGLE_SCOPES = ('https://www.googleapis.com/auth/userinfo.email '
                 'https://www.googleapis.com/auth/userinfo.profile')
GOOGLE_LOGIN_REDIRECT_URI = (f'{GOOGLE_OAUTH_ENDPOINTS['init_url']}?'
                             f'client_id={GOOGLE_CLIENT_ID}&'
                             f'redirect_uri={GOOGLE_REDIRECT_URI}&'
                             f'response_type=code&'
                             f'scope={GOOGLE_SCOPES}&'
                             f'access_type=offline')
