from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .backends import GoogleAuthBackend
from .constants import GOOGLE_LOGIN_REDIRECT_URI

User = get_user_model()


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def google_login(request):
    return HttpResponseRedirect(GOOGLE_LOGIN_REDIRECT_URI)


def google_callback(request):
    if 'code' in request.GET:
        user = authenticate(request,
                            code=request.GET.get('code'),
                            backend=GoogleAuthBackend)
        login(request, user=user)
        return redirect('core:index')
    else:
        return redirect('core::index')
