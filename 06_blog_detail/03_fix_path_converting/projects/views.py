from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)

def detail_slug(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404
    context = {'project': project}
    return render(request, 'projects/detail.html', context)