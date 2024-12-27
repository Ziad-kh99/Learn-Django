from django.shortcuts import render         # used to reneder templates.
from django.http import HttpResponse
from .models import Project


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



