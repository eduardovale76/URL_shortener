from django.shortcuts import render


def index(request):
    return render(request, "base/index.html")


def shortner(request):

    original_url = request.POST["urlorigin"]

    return render(request, "base/shortner.html", {"original_url": original_url})
