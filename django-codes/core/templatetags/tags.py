from django.template import Library
from stories.models import Category, Recipe

register = Library()

@register.simple_tag
def get_categories(limit = 5):
    return Category.objects.all()[:limit]


@register.filter
def upper(value):
    return value.upper()


@register.inclusion_tag('includes/latest_recipes.html')
def get_latest_recipes(limit = 5):
    latest_recipes = Recipe.objects.order_by('-created_at')[:limit]
    return {
        'latest_recipes' : latest_recipes
    }