from django import forms
from article.models import *
class Articleform(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','category','content',]
