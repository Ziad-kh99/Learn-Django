from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


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



