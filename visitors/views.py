from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from visitors.models import Visitor
from .forms import VisitorForm
# Create your views here.


def register_visitor(request):
    form = VisitorForm()

    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.registered_by = request.user.gatekeeper
            visitor.save()
            messages.success(
                request,
                "O visitante foi criado com sucesso."
            )
            return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'register_visitor.html', context)


def get_visitor(request, id):
    visitor = get_object_or_404(
        Visitor,
        id=id
    )
    context = {
        "visitor": visitor
    }
    return render(request, 'get_visitor.html', context)
