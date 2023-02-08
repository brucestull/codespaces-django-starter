from django.shortcuts import render

def index(request):
    """
    `index` view function, renders the `index.html` template.
    """
    context = {
            "title": "codespaces-django-starter",
    }
    return render(
        request,
        "index.html",
        context,
    )
