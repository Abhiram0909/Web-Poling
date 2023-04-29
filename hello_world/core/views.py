from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )


def login(request):
    return render(
        request,
        "login.html"
    )

def click(request):
    return render(
        request,
        "login.html"
    )