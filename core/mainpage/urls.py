from django.urls import path
from django.views.generic import RedirectView
from .views import steins_gate_page, steins_gate_zero_page

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='steins_gate_page')),
    path("steins-gate/", steins_gate_page, name="steins_gate_page"),
    path("steins-gate-zero/", steins_gate_zero_page, name="steins_gate_zero_page")
]
