from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'user_login/$', views.index, name='index'),
]