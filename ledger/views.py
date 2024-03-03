from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe
# Create your views here.
    
class  RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe.html'

class RecipeDetailView (DetailView):
    model=Recipe
    template_name='recipeDetail.html'


def recipeList(request):
    # Get the list of all Recipe objects
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
        }

    return render(request, "recipe.html", ctx)
def recipeDetail(request,id):
    ctx = {
        'recipes', Recipe.objects.get(id=id)
        
    }
    return render(request,"recipeList.html",ctx)

