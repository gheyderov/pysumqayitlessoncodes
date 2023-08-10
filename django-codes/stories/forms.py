from django import forms
from stories.models import Comment, Recipe

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'image',
            'cover_image',
            'small_description',
            'description',
            'category',
            'tags'
        )
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title',
            }),
            'image' : forms.FileInput,
            'cover_image' : forms.FileInput,
            'small_description' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Small Description',
            }),
            'description' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Description',
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'tags' : forms.SelectMultiple(attrs={
                'class' : 'form-control',
            }),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Content',
                'cols' : 30,
                'rows' : 7
            })
        }
    

class SubCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Content',
                'cols' : 30,
                'rows' : 7
            })
        }
