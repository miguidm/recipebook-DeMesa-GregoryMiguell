from django.urls import path
from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('recipes/list',RecipeListView.as_view(), name ='recipe'),
    path('recipe/<int:pk>/list', RecipeDetailView.as_view(), name = "<int:pk>/detail"),
]

app_name = "ledger"