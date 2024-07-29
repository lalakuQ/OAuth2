from .constants import GOOGLE_OAUTH_ENDPOINTS


def get_google_user_details_url(access_token):
    return f'{GOOGLE_OAUTH_ENDPOINTS['info_url']}?access_token={access_token}'
