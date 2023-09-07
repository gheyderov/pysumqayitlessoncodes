from django.urls import path
from stories.api.views import (
    categories,
    RecipeAPIView,
    RecipeRetrieveUpdateDeleteAPIView,
    CategoryAPIView,
    TagAPIView
)
from stories.api.routers import router

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('recipes/', RecipeAPIView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeRetrieveUpdateDeleteAPIView.as_view(), name='recipe_update'),
]

# urlpatterns += router.urls