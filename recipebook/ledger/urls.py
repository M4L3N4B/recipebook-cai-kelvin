from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_create, name='recipe_create'),
    path('ingredient/add/', views.ingredient_add, name='ingredient_add'),
    path('recipe/<int:pk>/add_image/', views.recipe_image_add, name='recipe_image_add')
]
