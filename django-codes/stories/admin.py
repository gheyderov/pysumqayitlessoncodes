from django.contrib import admin
from stories.models import Recipe, Category, Tag, RecipeImage
from django import forms


# Register your models here.


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'tags' : forms.CheckboxSelectMultiple
        }


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(RecipeImage)


class RecipeInline(admin.TabularInline):
    model = RecipeImage



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    list_filter = ['category', 'tags']
    search_fields = ['title', 'category__title']
    inlines = [RecipeInline]
    form = RecipeAdminForm

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