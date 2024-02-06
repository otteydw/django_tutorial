from django.shortcuts import render

posts = [
    {
        "author": "DanO",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "February 1, 2024",
    },
    {
        "author": "JanetO",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "February 2, 2024",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context=context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
