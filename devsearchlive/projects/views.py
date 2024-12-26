from django.shortcuts import render         # used to reneder templates.
from django.http import HttpResponse

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
    name = 'Ziad Khaled'

    context = {
        'name': name,
        'projects': projectsList
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = None

    for project in projectsList:
        if project['id'] == pk:
            projectObject = project

    context = {
        'project': projectObject,
        'pk': pk
    }

    return render(request, 'projects/single_project.html', context)



