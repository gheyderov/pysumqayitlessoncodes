from django.shortcuts import render, get_object_or_404
from stories.models import Recipe, Category, Tag

# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'categories' : categories
    }
    return render(request, 'recipes.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    tags = Tag.objects.all()
    context = {
        'recipe' : recipe,
        'tags' : tags
    }
    return render(request, 'single.html', context)
