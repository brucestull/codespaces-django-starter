from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "My own pesonal Django Example!",
        },
    )
