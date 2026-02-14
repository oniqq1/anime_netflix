from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import AnimeDescription , Comment
from django.core.paginator import Paginator


def steins_gate_page(request):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        if comment_text:
            Comment.objects.create(
                user=request.user,
                anime=AnimeDescription.objects.get(name="Steins;Gate"),
                text=comment_text
            )

    anime, created = AnimeDescription.objects.get_or_create(
        name="Steins;Gate",
        defaults={
            "appearing": "2011 весна",
            "type": "ТВ (25 эп.), 25 мин.",
            "genres": "Триллер, Фантастика, Научная фантастика, Тайна, Психологический хоррор, Приключение, Романтика",
            "description": """В Вратах Штейна рассказывается о группе молодых студентов-технарей.
        Студенты находят способ менять прошлое по почте с помощью модифицированной микроволновки и начинают опыты с целью узнать,
        насколько далеко сможет зайти их открытие, но в итоге все начинает выходить из-под контроля,
        и студенты впутываются в заговор вокруг SERN — организации, стоящей за Большим адронным коллайдером — и Джона Титора,
        утверждающего, что он явился из антиутопичного будущего.""",
        },
    )
    comments = Comment.objects.filter(anime=anime).order_by("-created_at")

    paginator = Paginator(comments, 6)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    return render(request, "steins-gate_page.html", {"anime": anime , "comments": comments})

def steins_gate_zero_page(request):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        if comment_text:
            Comment.objects.create(
                user=request.user,
                anime=AnimeDescription.objects.get(name="Steins;Gate 0"),
                text=comment_text
            )

    anime, created = AnimeDescription.objects.get_or_create(
        name="Steins;Gate 0",
        defaults={
            "appearing": "2018 весна",
            "type": "ТВ (24 эп.), 25 мин.",
            "genres": "Триллер, Фантастика, Научная фантастика, Тайна, Психологический хоррор, Психология, Романтика",
            "description": """Альтернативная концовка Врат Штейна
        в которой эгоцентричный безумный ученый Окабе Ринтаро изо всех сил старается оправиться от неудачной попытки спасти жизнь Курису Макисе.
        Стараясь забыть прошлое, Окабе отказывается от своего альтер-эго. И когда, казалось бы, всё наладилось, он снова сталкивается со своим прошлым.
        Он знакомится с девушкой, которая представилась знакомой Курису.
        От неё Окабе узнает, что в данный момент проходит испытание устройства, которое способно воссоздавать характер и личность человека по воспоминаниям.
        Начиная тестирование он и не предполагал, что воссоздание Курису принесет столько мучений и новых неожиданных последствий..."""
        }
    )
    comments = Comment.objects.filter(anime=anime).order_by("-created_at")

    paginator = Paginator(comments, 6)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    return render(request, "steins-gate-zero_page.html", {"anime": anime , "comments": comments})