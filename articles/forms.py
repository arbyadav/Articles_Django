from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('article_id', 'title', 'body', 'pub_date', 'thumbnail')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')
