from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Dan",
        "title": "Blog Post 1",
        "content": "First Post content",
        "date_posted": "July 6, 2023",
    },
    {
        "author": "Janet",
        "title": "Blog Post 2",
        "content": "Second Post content",
        "date_posted": "July 7, 2023",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html.j2", context)


def about(request):
    return render(request, "blog/about.html.j2", {"title": "About"})
