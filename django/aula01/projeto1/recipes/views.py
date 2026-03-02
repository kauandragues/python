from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(
        request=request,
        template_name="recipes/home.html",
        context={"name": "Kauã Andrade"},
        status=201,
    )


def contato(request):
    return HttpResponse("<h1>CONTATO</h1>")


def sobre(request):
    return HttpResponse("<h1>SOBRE</h1>")
