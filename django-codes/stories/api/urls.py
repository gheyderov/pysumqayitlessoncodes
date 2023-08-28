from django.urls import path
from stories.api.views import (
    categories,
    RecipeAPIView,
    RecipeRetrieveUpdateDeleteAPIView
)
from stories.api.routers import router

urlpatterns = [
    path('categories/', categories, name='categories'),
    # path('recipes/', RecipeAPIView.as_view(), name='recipes'),
    # path('recipe/<int:pk>/', RecipeRetrieveUpdateDeleteAPIView.as_view(), name='recipe_update'),
]

urlpatterns += router.urls