from django import forms
from .models import Article

from ckeditor.widgets import CKEditorWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['name', 'text', 'products', 'author']