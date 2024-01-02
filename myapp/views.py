from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject
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
    return render (request, 'project/projects.html', {
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render (request, 'task/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, "task/create_task.html", {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(tittle=request.POST['tittle'], description=request.POST['description'], project_id=2)
        return redirect('task/tasks/')

def create_project(request):
    if request.method =='GET':
        return render(request, 'project/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')