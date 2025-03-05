from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<str:name>/', views.recipe_detail, name='recipe_detail'),
]
