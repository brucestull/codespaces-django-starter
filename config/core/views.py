from django.shortcuts import render

def index(request):
    """
    `index` view function, renders the `index.html` template.
    """
    context = {
            "title": "animated-palm-tree",
    }
    return render(
        request,
        "index.html",
        context,
    )
