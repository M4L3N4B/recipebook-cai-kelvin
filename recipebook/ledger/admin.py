from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('name', )


# Allows editing of recipe ingredients while a recipe entry is being edited
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('name', )
    inlines = [RecipeIngredientInline]
    

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe__name', 'ingredient__name', )
    list_display = ('ingredient', 'quantity', 'recipe')
    list_filter = ('recipe', 'ingredient', )
    
    # Creates fields when adding new a recipe ingredient
    fieldsets = [
        ('Details', {
            'fields': [
                ('ingredient', 'quantity'), 'recipe'
            ],
        }),
    ]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
