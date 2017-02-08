from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    if request.method == "GET":
        context = {
            "todos": Todo.objects.all()
        }
        return render(request, 'todoapp/index.html', context)
    elif request.method == "POST":
        new_todo = Todo()
        new_todo.text = request.POST["text"]
        new_todo.save()
        return redirect('index')
