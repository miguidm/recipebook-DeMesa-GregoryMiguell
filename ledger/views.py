from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Ingredient, Recipe, RecipeIngredient

from .models import Recipe
# Create your views here.
    
class  RecipeListView(ListView):
    model = Recipe
    template_name = 'recipeList.html'

class RecipeDetailView (DetailView):
    model = Recipe
    template_name = 'recipe.html'


def recipeList(request):
    # Get the list of all Recipe objects
    recipes = Recipe.objects.all()
    ctx = {
        "recipe": recipes
        }

    return render(request, "recipeList.html", ctx)

def recipeDetail(request,pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'recipe': recipe
        }
    return render(request,"recipe.html",ctx)

