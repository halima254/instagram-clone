from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post,Profile,Comment,Like
from django.contrib.auth.models import User

# Create your views here.
