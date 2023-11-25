from django.db import models
from django.shortcuts import render
from .models import BlogPost

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})
