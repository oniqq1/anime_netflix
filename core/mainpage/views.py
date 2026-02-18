from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import AnimeDescription, Comment
from .constants import ANIME_DEFAULTS, ANIME_POSTERS, ANIME_PLAYERS, ANIME_QUESTIONS
import logging
import bleach

logger = logging.getLogger(__name__)

def _anime_page(request, anime_name, template):
    anime, _ = AnimeDescription.objects.get_or_create(name=anime_name,defaults=ANIME_DEFAULTS[anime_name],)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(request.path)
        comment_text = request.POST.get("comment", "").strip()
        # Отчистка от html тегов
        comment_text = bleach.clean(comment_text, tags=[], strip=True)
        if comment_text and len(comment_text) < 2000:
            Comment.objects.create(user=request.user, anime=anime, text=comment_text)
            logger.info(f"Anime {anime_name} comment {comment_text} , user={request.user.username}" )
        return redirect(request.path)

    comments = anime.comments.select_related("user", "user__profile")
    paginator = Paginator(comments, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    poster = ANIME_POSTERS.get(anime_name, "")
    players = ANIME_PLAYERS.get(anime_name, {})

    return render(request, template, {"anime": anime, "comments": page_obj, "poster": poster, "players": players, "questions": ANIME_QUESTIONS})

def steins_gate_page(request):
    logger.info(f"Steins Gate page opened , user={request.user.username if request.user.is_authenticated else None}")
    return _anime_page(request, "Steins;Gate", "steins-gate_page.html")

def steins_gate_zero_page(request):
    logger.info(f"Steins Gate zero page opened , user={request.user.username if request.user.is_authenticated else None}")
    return _anime_page(request, "Steins;Gate 0", "steins-gate-zero_page.html")

def steins_gate_load_region_page(request):
    logger.info(f"Steins Gate: Load Region of Déjà Vu page opened , user={request.user.username if request.user.is_authenticated else None}")
    return _anime_page(request, "Steins;Gate: Load Region of Deja Vu", "steins_gate_load_region_page.html")

def steins_gate_missing_link(request):
    logger.info(f"Steins Gate: Kyoukaimenjou no Missing Link, user={request.user.username if request.user.is_authenticated else None}")
    return _anime_page(request, "Steins;Gate: Kyoukaimenjou no Missing Link", "steins_gate_missing_link.html")

def future_gadget_laboratory_page(request):
    logger.info(f"Future Gadget Laboratory page opened , user={request.user.username if request.user.is_authenticated else None}")
    return render(request, "future_gadget_laboratory.html")