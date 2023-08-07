from django.urls import path
from stories.views import recipes, recipe_detail, like_post, RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),


]
