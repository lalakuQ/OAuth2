from django.urls import include, path
from . import views


app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('google/login/', views.google_login, name='glogin'),
    path('google/callback/', views.google_callback, name='callback'),
]