from math import log
import re
from urllib import request

from django.shortcuts import render, redirect
from django.urls import is_valid_path
from .models import BlogPost
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from dotenv import load_dotenv
import os

def u_creds():
    load_dotenv()
    username = os.getenv('SECRET_USER')
    password = os.getenv('SECRET_PASS')
    

def index(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    return render(request, 'index.html', {'posts': posts})


def login_view(request):
    if request.method == 'POST':
        username = request.POST[u_creds.username]
        password = request.POST[u_creds.password]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})
