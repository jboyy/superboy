from blogcomment import models
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model= models.BlogComment
        fields = ['name','content']