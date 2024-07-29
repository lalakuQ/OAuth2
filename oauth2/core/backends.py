import json

import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

from .constants import (GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
                        GOOGLE_OAUTH_ENDPOINTS, GOOGLE_REDIRECT_URI)
from .utils import get_google_user_details_url

User = get_user_model()


class GoogleAuthBackend(BaseBackend):
    def _get_access_token(self, code=None):
        response = requests.post(url=GOOGLE_OAUTH_ENDPOINTS['token_url'],
                                 data={
                                    'code': code,
                                    'client_id': GOOGLE_CLIENT_ID,
                                    'client_secret': GOOGLE_CLIENT_SECRET,
                                    'redirect_uri': GOOGLE_REDIRECT_URI,
                                    'grant_type': 'authorization_code'
                                })
        access_token = json.loads(response.content)['access_token']
        return access_token

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def authenticate(self,
                     request,
                     username=None,
                     password=None,
                     code=None,
                     **kwargs):
        if code:
            access_token = self._get_access_token(code=code)
            if access_token:

                g_user_details = requests.get(
                    get_google_user_details_url(access_token))

                user, created = User.objects.get_or_create(
                    username=g_user_details.json().get('email'))
                return user
