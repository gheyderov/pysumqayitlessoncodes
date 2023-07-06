from django.shortcuts import render
from stories.models import Recipe, Category

# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()[:3]
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'categories' : categories
    }
    return render(request, 'recipes.html', context)


def single(request):
    return render(request, 'single.html')
