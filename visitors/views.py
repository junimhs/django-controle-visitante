from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from visitors.models import Visitor
from .forms import (
    VisitorForm,
    AuthorizationVisitorForm
)

from django.http import HttpResponseNotAllowed

from django.utils import timezone
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

    form = AuthorizationVisitorForm()

    if request.method == 'POST':
        form = AuthorizationVisitorForm(request.POST, instance=visitor)

        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.status = "EM_VISITA"
            visitor.authorization_time = timezone.now()
            visitor.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso."
            )

            return redirect("index")

    context = {
        "visitor": visitor,
        "form": form
    }
    return render(request, 'get_visitor.html', context)


def finish_visitor(request, id):
    visitor = get_object_or_404(
        Visitor,
        id=id
    )

    if request.method == 'POST':
        visitor.status = "FINALIZADO"
        visitor.departure_time = timezone.now()

        visitor.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect("index")
    else:
        return HttpResponseNotAllowed(
            ['POST'],
            "Metodo não permitido"
        )
