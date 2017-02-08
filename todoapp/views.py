from django.contrib.auth.models import User
from django.contrib import auth

from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    context = {
        "todos": Todo.objects.all()
    }
    print("user:", request.user.username)
    return render(request, 'todoapp/index.html', context)
    
def signup(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/signup.html', context)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                return login(request)
        except:
            context["error"] = f"Username '{username}' already exists."
            return render(request, 'todoapp/signup.html', context)
    
def login(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/login.html')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
            
def logout(request):
    auth.logout(request)
    return redirect('index')
