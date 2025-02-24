from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_num>/', views.recipe_preview, name='recipe_preview'),
]
