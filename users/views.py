from django.shortcuts import render

# Create your views here.
from visitors.models import Visitor


def index(request):
    visitors = Visitor.objects.all()
    context = {
        'visitors': visitors
    }
    return render(request, 'index.html', context)
