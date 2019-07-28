from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.usersignup, name='register_user'),  
    ]