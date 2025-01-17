from django.http import HttpResponse
from .models import Buyer, Game


# def homepageview(request):
#     return HttpResponse('Hello world')

def index(request):
    return HttpResponse('<a href="index1">Hello worldzzzzzzzzzz!!!</a>')

def index1(request):
    Buyer.objects.create(
        name="Ilya",
        balance=1500.05,
        age=24
    )
    Buyer.objects.create(
        name="Termonator2000",
        balance=42.15,
        age=52
    )
    Buyer.objects.create(
        name="Ubivator432",
        balance=0.5,
        age=16
    )
    Game.objects.create(
        title="Cyberpunk 2077",
        cost=31,
        size=46.2,
        description = 'Game of the year',
        age_limited = True
    )
    Game.objects.create(
        title="Mario",
        cost=5,
        size=0.5,
        description='Old game',
        age_limited=False
    )
    Game.objects.create(
        title="Hitman",
        cost=12,
        size=36.6,
        description='Who kills Mark?',
        age_limited=True
    )

    first_buyer = Buyer.objects.get(id=1)
    second_buyer = Buyer.objects.get(id=2)
    free_buyer = Buyer.objects.get(id=3)

    Game.objects.get(id=1).buyer.set((first_buyer, second_buyer))
    Game.objects.get(id=2).buyer.set((second_buyer, free_buyer))
    Game.objects.get(id=3).buyer.set((first_buyer, second_buyer))
    #Buyer.set((first_buyer, second_buyer))
    return HttpResponse('Hello world!!!')