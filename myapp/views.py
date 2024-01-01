from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render (request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render (request, 'task.html', {
        'tasks': tasks
    })