from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# All tasks
def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todos/all_tasks.html', {'tasks': tasks})

# Create new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('all_tasks')
    else:
        form = TaskForm()
    return render(request, 'todos/task_form.html', {'form': form})

# Details of task
def task_details(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('all_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todos/task_form.html', {'form': form})