from django.contrib import admin
from .models import Profile, Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class RecipeImageInline(admin.StackedInline):
    model = RecipeImage


# Allows editing of recipe ingredients while a recipe entry is being edited
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]
    

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('name', )
    inlines = [RecipeIngredientInline, RecipeImageInline]
    

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

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
