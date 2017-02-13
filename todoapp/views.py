from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Todo, Tag

# Create your views here.
def index(request):
    if request.method == "GET":
        context = {
            "todos": Todo.objects.filter(user_id=request.user).select_related()
        }
        return render(request, 'todoapp/index.html', context)
    elif request.method == "POST":
        if request.user.is_authenticated:
            new_todo = Todo()
            new_todo.text = request.POST["text"]
            tag, created = Tag.objects.get_or_create(name=request.POST["tag"])
            new_todo.user_id = request.user.id
            new_todo.save()
            new_todo.tags.add(tag)
            return redirect('index')
        else:
            return redirect('/login')

def signup(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/signup.html', context)
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                return login(request)
        except:
            context["error"] = f"User {username} already exists"
            return render(request, 'todoapp/signup', context)

def login(request):
    if request.method == "GET":
        return render(request, 'todoapp/login.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def secret(request):
    context = {"error": False}
    if request.user.is_authenticated:
        return render(request, 'todoapp/secret.html')
    else:
        context["error"] = "Not authenticated"
        return render(request, 'todoapp/signup.html', context)
