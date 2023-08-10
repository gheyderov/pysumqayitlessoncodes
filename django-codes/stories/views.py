from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from stories.models import Recipe, Category, Tag
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from stories.forms import CommentForm, SubCommentForm, RecipeCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    # success_url = reverse_lazy('recipes')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class RecipeUpdateView(UpdateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    model = Recipe


def recipes(request):
    print('Liked posts: ', request.session.get('liked_posts'))
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'categories' : categories
    }
    return render(request, 'recipes.html', context)


class RecipeListView(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-created_at']
    paginate_by = 1
    # recipe_list
    # Recipe.objects.all

    def get_queryset(self) -> QuerySet[Any]:
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        queryset = super().get_queryset()
        if cat_id:
            queryset = queryset.filter(category__id = cat_id)
        if tag_id:
            queryset = queryset.filter(tags__id = tag_id)
        if cat_id and tag_id:
            queryset = queryset.filter(category__id = cat_id, tags__id = tag_id)
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    tags = Tag.objects.all()
    context = {
        'recipe' : recipe,
        'tags' : tags
    }
    return render(request, 'single.html', context)


class RecipeDetailView(FormMixin, DetailView):
    template_name = 'single.html'
    model = Recipe
    form_class = CommentForm
    subform = SubCommentForm
    # success_url = reverse_lazy('recipe_detail')

    def get_success_url(self) -> str:
        return reverse_lazy('recipe_detail', kwargs = {'pk' : self.object.pk})

    def post(self, request, *args, **kwargs):
        if 'parent' in request.POST:
            self.form_class = self.subform
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.parent_id = self.request.POST.get('parent', None)
        form.instance.recipe = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked!")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('like')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response