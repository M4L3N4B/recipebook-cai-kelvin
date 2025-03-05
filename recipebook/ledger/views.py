from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.get(name=recipe_name)
    ctx = {'recipe': recipe}
    return render(request, 'recipe_detail.html', ctx)
