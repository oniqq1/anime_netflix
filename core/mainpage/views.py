from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def steins_gate_page(request: HttpRequest) -> HttpResponse:
    return render(request, "steins-gate_page.html")

def steins_gate_zero_page(request: HttpRequest) -> HttpResponse:
    return render(request, "steins-gate-zero_page.html")
