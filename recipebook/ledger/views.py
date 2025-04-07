from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, IngredientForm, RecipeIngredientFormSet


@login_required
def home(request):
    return redirect('login')
    

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'ledger/recipe_list.html', ctx)


@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ctx = {'recipe': recipe}
    return render(request, 'ledger/recipe_detail.html', ctx)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        
        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            formset.instance = recipe
            formset.save()
            
            return redirect(recipe.get_absolute_url())
    else:
        recipe_form = RecipeForm()
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
    
    ctx = {'recipe_form': recipe_form, 'formset': formset}
    return render(request, 'ledger/recipe_create.html', ctx)
    

@login_required
def ingredient_add(request):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save()
            return redirect('recipe_create')
    else:
        ingredient_form = IngredientForm()
        
    return render(request, 'ledger/ingredient_add.html', {'ingredient_form': ingredient_form})
