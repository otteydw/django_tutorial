from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html.j2", context)


def about(request):
    return render(request, "blog/about.html.j2", {"title": "About"})
