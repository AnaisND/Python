from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_words})
