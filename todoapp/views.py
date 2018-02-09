from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Main routes
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all().order_by("text")
        users = User.objects.all()
        return render( request, 'todoapp/index.html', {"todos":todos,"users":users})
    elif request.method == "POST":
        return HttpResponse('index POST')

def delete(request, todo_id):
    return HttpResponse("Delete this")

def done(request, todo_id):
    return HttpResponse("Mark done")

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request,"todoapp/signup.html")
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        try:
            user = User.objects.create_user(username=username, password=password, first_name=firstname)
            if user is not None:
                return login(request)
        except:
            return render(request, "todoapp/signup.html", {"error":"Username already exists"})
        return HttpResponse('Posted to signup')

def login(request):
    if request.method == 'GET':
        return render(request,"todoapp/login.html")
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            return render( request, "todoapp/login.html", {"error": " Invalid Credentials"})

def logout(request):
    auth.logout(request)
    return redirect("index")
