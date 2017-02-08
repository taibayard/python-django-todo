from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    context = {
        "todos": Todo.objects.all()
    }
    return render(request, 'todoapp/index.html', context)
