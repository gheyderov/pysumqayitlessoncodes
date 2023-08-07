from django import forms
from stories.models import Comment


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
