from django.shortcuts import render, redirect
from .models import User

def index(request):
    users = { 'list':User.objects.all() }
    print users
    return render(request, 'user_login_app/index.html', users)
