from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import AnimeDescription, Comment
from .constants import ANIME_DEFAULTS

def _anime_page(request, anime_name, template):
    anime, _ = AnimeDescription.objects.get_or_create(name=anime_name,defaults=ANIME_DEFAULTS[anime_name],)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(request.path)
        comment_text = request.POST.get("comment", "").strip()
        if comment_text:
            Comment.objects.create(user=request.user, anime=anime, text=comment_text)
        return redirect(request.path)

    comments = anime.comments.select_related("user", "user__profile")
    paginator = Paginator(comments, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, template, {"anime": anime, "comments": page_obj})


def steins_gate_page(request):
    return _anime_page(request, "Steins;Gate", "steins-gate_page.html")


def steins_gate_zero_page(request):
    return _anime_page(request, "Steins;Gate 0", "steins-gate-zero_page.html")
