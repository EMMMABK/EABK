from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'eabk/index.html', {'title': 'Main page of this site', 'tasks': tasks})

def about(request):
    return render(request, 'eabk/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was wrong'

    form = TaskForm()
    context = {
        'form':form,
        'error': error
    }
    return render(request, 'eabk/create.html', context)
