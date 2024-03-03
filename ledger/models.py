from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here
# 
class Recipe(models.Model):
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:ingredient',args=[str(self.pk)])
class  Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe',args=[str(self.pk)])
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name= "ingredient")
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name= 'recipe')