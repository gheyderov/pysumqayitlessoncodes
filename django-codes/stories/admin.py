from django.contrib import admin
from stories.models import Recipe, Category, Tag, RecipeImage, Comment
from django import forms
from modeltranslation.admin import TranslationAdmin


# Register your models here.


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'tags' : forms.CheckboxSelectMultiple
        }



admin.site.register(Tag)
admin.site.register(RecipeImage)
admin.site.register(Comment)

class CategoryAdmin(TranslationAdmin):
    list_display = ['title']

admin.site.register(Category, CategoryAdmin)


class RecipeInline(admin.TabularInline):
    model = RecipeImage



@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'category', 'author', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    list_filter = ['category', 'tags']
    search_fields = ['title', 'category__title']
    inlines = [RecipeInline]
    form = RecipeAdminForm
    readonly_fields = ['slug']

    def get_tags(self, obj):
        arr = []
        for tag in obj.tags.all():
            arr.append(tag)
        return arr
    
    # fieldsets = [
    #     (
    #         'Main Fields',
    #         {
    #             "fields": ["title", "category", "description"],
    #         },
    #     ),
    #     (
    #         "Other Fields",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["image", "cover_image"],
    #         },
    #     ),
    # ]