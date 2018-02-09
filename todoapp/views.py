from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Main routes
def index(request):
    if request.method == "GET":
        return HttpResponse('index GET')
    elif request.method == "POST":
        return HttpResponse('index POST')

def delete(request, todo_id):
    return HttpResponse("Delete this")

def delete(request, todo_id):
    return HttpResponse("Mark done")

# Auth-related routes
def signup(request):
    return HttpResponse('signup')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')
