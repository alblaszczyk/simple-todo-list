from django.shortcuts import render, get_object_or_404, redirect
from todolist.models import ToDoList, Task
from todolist.forms import ToDoListForm, TaskForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json



def main_view(request):
    todo_lists = ToDoList.objects.order_by('name')
    return render(request, 'todolist/todo_lists.html', {'todo_lists': todo_lists})


def list_view(request, pk):
    todo_list = ToDoList.objects.get(pk=pk)
    todo_list_name = ToDoList.objects.get(pk=pk)
    todo_list = todo_list.id
    tasks = Task.objects.filter(todo_list=pk).order_by('name')
    return render(request, 'todolist/task_list.html', {'tasks': tasks, 'todo_list': todo_list, 'todo_list_name': todo_list_name})

def todo_list_new(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            todo_list.save()
            return redirect('list_view', pk=todo_list.pk)
    else:
        form = ToDoListForm()
        return render(request, 'todolist/edit_list.html', {'form': form})

def todo_list_remove(request, pk):
    todo_list = get_object_or_404(ToDoList, pk=pk)
    todo_list.delete()
    return redirect('main')

def create_task(request, pk):
    todo_list = get_object_or_404(ToDoList, pk=pk)
    # todo_list = todo.id
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.todo_list = todo_list
            task.save()
            return redirect('list_view', pk=todo_list.id)
    else:
        form = TaskForm()
    return render(request, 'todolist/create_task.html', {'form': form})


def remove_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    foreignkey = task.todo_list
    task.delete()
    return redirect('list_view', pk=foreignkey.id)


def task_do(request):
    task = get_object_or_404(Task, pk=pk)
    foreignkey = task.todo_list
    task.done()
    return redirect('list_view', pk=foreignkey.id)

@ensure_csrf_cookie
def done_task(request):
    data = json.loads(request.body)
    task_id = int(data['taskId'][0])
    task = Task.objects.get(id=task_id)
    task.task_done = True
    task.save()
    return JsonResponse({'taskId': task.id})
