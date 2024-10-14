from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


# posts = [
#     {
#         'author': 'ziad khaled'.title(),
#         'title': 'Blog Post 1',
#         'content': 'Firt post content...',
#         'date_posted': 'August 5, 2022'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content...',
#         'date_posted': 'April 27, 2023'
#     },
#     {
#         'author': 'Ramy Hafez',
#         'title': 'Blog Post 3',
#         'content': 'Third post content...',
#         'date_posted': 'June 13, 2023'
#     },
# ]


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'AZ-Blog Home',
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'AZ-Blog About'})
    # return HttpResponse('<h1>About Page</h1>')



