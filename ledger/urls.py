from django.urls import path
from .views import RecipeDetailView, RecipeListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('recipes/list',RecipeListView.as_view(), name ='recipeList'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name = "recipe"),
    
]

app_name = "ledger"