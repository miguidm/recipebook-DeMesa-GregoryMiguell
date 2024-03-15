from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
# Create your views here.
    
class  RecipeListView(ListView):
    model = Recipe
    template_name = 'recipeList.html'

class RecipeDetailView (LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = '/recipes/list'
