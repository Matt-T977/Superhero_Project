from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes,
    }
    return render(request, "superheroes/index.html", context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero' : single_hero,
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        catch_phrase = request.POST.get('catch_phrase')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        new_hero = Superhero(name=name, alter_ego=alter_ego, catch_phrase=catch_phrase, primary_ability=primary_ability, secondary_ability=secondary_ability)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def update(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        catch_phrase = request.POST.get('catch_phrase')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        single_hero = single_hero(name=name, alter_ego=alter_ego, catch_phrase=catch_phrase, primary_ability=primary_ability, secondary_ability=secondary_ability)
        single_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else: 
        return render(request, 'superheroes/update.html')
