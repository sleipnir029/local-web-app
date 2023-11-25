from math import log
from urllib import request
from webbrowser import get

from django.shortcuts import render, redirect
from django.urls import is_valid_path
from .models import BlogPost
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from dotenv import load_dotenv
import os
from django.http import HttpResponse
 

def index(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    return render(request, 'index.html', {'posts': posts})


def login_view(request):
    if request.method == 'POST':
        #load_dotenv()
        #u_ser = os.getenv("SECRET_USER")
        #p_word = os.getenv("SECRET_PASS")
        username = request.POST.get("username")
        password = request.POST.get("password")
        #print(u_ser,p_word)
        #print(username, password)
        #print("before")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #print('after')
            return redirect('index')  # Redirect to the dashboard page upon successful login
            #return HttpResponse("Authentication successful")
        else:
            # Provide an error message for incorrect credentials
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error': error_message})
            #return HttpResponse("Authentication failed")
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
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})
