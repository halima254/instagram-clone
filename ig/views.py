from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post,Profile,Comment,Like
from .forms import PostForm, ProfileForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    template = loader.get_template('ig/home.html')
        
    if request.user.is_anonymous:
         Context = {}
         return HttpResponse(template.render(context,request)) 
    posts = Post.objects.all()
    profile = Profile.objects.get(user= request.user)
    comments = Comment.objects.all()
    context = {'posts':posts, 'profile':profile,'comments':comments}
    
    return HttpResponse(template.render(context,request))
