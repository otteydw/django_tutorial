from django.shortcuts import render
# import pokebase as pb
import random

import pokebase as pb
from pokebase import cache
cache.API_CACHE

def home(request):
    mon_number = random.randint(1, 1010)
    mon = pb.pokemon(mon_number)
    sprite = pb.SpriteResource('pokemon', mon_number)
    context = {'mon': mon, "sprite": sprite}
    return render(request, "pokemon/home.html.j2", context)
