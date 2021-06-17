from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)


def detail(request, pk):
    # TODO: how can I get a single object from the database again?
    # DONE
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)
