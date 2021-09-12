from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'context': 'from context'
    }
    return render(request, 'posts/index.html', context)
