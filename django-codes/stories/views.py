from django.shortcuts import render, get_object_or_404, HttpResponse
from stories.models import Recipe, Category, Tag
from django.contrib import messages

# Create your views here.

def recipes(request):
    print('Liked posts: ', request.session.get('liked_posts'))
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


# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked!")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('like')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response