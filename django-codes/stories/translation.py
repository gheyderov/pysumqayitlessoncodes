from modeltranslation.translator import translator, TranslationOptions
from stories.models import Category, Recipe

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Category, CategoryTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)