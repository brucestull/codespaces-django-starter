from django.shortcuts import render

def index(request):
    """
    `index` view function, renders the `index.html` template.
    """
    context = {
            "title": "My own personal Django Example!",
    }
    return render(
        request,
        "index.html",
        context,
    )
