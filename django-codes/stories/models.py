from django.db import models
from core.models import AbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Recipe(AbstractModel):
    category = models.ForeignKey(
        'Category', related_name='recipes', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=100)
    small_description = models.CharField('small_description', max_length=155)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='recipe_images/')
    cover_image = models.ImageField('cover_image', upload_to='recipe_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class RecipeImage(AbstractModel):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name='images')
    image = models.ImageField('image', upload_to='recipe_images/')

    def __str__(self) -> str:
        return self.recipe.title
    


class Category(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('title', max_length=100)

    def __str__(self):
        if self.parent:
            return f'{self.parent} | {self.title}'
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # ordering = ['-created_at']


class Tag(AbstractModel):
    title = models.CharField('title', max_length=100)

    def __str__(self):
        return self.title
