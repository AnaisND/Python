from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def wordcounter(request):
    words = request.GET["words"]
    n = len(words.split())
    return render(request, "wordcounter.html", {"amount" : n})