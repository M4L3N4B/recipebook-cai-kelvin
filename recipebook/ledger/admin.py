from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('name', )
    

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe__name', 'ingredient__name', )
    list_display = ('recipe', 'ingredient', 'quantity', )
    list_filter = ('recipe', 'ingredient', )
    fieldsets = [
        ('Details', {
            'fields': [
                'recipe', ('ingredient', 'quantity'),
            ],
        }),
    ]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
