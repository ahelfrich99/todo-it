from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from projects.forms import CreateProjectForm


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    task = Task.objects.filter(project=project)
    context = {"project": project, "task": task}
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()

    context = {"form": form}

    return render(request, "projects/create.html", context)
