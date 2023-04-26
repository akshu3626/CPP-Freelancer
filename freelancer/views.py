from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate , logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this


def home(request):
    return render(request , "index.html")
   