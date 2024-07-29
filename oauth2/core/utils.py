from .constants import OAUTH_ENDPOINTS


def get_google_user_details_url(access_token):
    return f'{OAUTH_ENDPOINTS['info_url']}?access_token={access_token}'
