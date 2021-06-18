from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)


def detail_pk(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)

def detail_slug(request, slug):
    project = Project.objects.get(slug=slug)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)