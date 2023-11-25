from django.shortcuts import render
from .models import BlogPost
from . import urls

def index(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    return render(request, 'index.html', {'posts': posts})