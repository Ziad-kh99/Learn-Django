from django.shortcuts import render, redirect      # used to reneder templates or redirect to another one.
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm 


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    projects = Project.objects.all()        # return all tuples in project model.
    # print(f'Projects: {projects}')
    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.reviews.all()

    context = {
        'project': projectObj,
        'tags': tags,
        'reviews': reviews,
        'pk': pk
    }

    return render(request, 'projects/single_project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')


    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/update_project.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_project.html', {'object': project})