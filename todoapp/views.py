from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
import requests
import json

# Main routes
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all().order_by("text")
        users = User.objects.all()
        r = requests.get("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&callback=")
        quote = json.loads(r.text)
        return render( request, 'todoapp/index.html', {"todos":todos,"users":users,"quote":quote[0]})
    elif request.method == "POST":
        try:
            userid=request.POST["userid"]
        except (KeyValueError):
            return redner(request, "todoapp/index.html", {"error":"You must select a owner"})
        else:
            new_todo =  Todo()
            new_todo.text = request.POST["text"]
            new_todo.user = User.objects.get(pk=userid)
            new_todo.save()
            return redirect("index")

def delete(request, todo_id):
    item = Todo.objects.get(id=todo_id)
    item.delete()
    return redirect("index")
    #Alternate syntax for delete
    #Todo.objects.filter(id=todo_id).delete()

def done(request, todo_id):
    item = Todo.objects.get(id=todo_id)
    item.is_complete = True
    item.save()
    return redirect("index")

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
