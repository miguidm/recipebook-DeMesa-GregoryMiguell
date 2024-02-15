from django.urls import path
from .views import index,recipeList, recipeOne, recipeTwo

urlpatterns = [
    path('',index, name ='index'),
    path('recipes/list', recipeList, name = "recipeList"),
    path('recipe/1',recipeOne, name = "recipeOne" ),
    path('recipe/2',recipeTwo, name ="recipeTwo"),
]

app_name = "ledger"