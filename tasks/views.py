from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()

    context = {"form": form}

    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    my_tasks = Task.objects.filter(assignee=request.user)
    context = {"my_tasks": my_tasks}
    return render(request, "tasks/list.html", context)
