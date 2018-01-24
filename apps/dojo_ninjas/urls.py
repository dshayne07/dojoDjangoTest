from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dojo_ninja/$', views.index, name='index'),
]