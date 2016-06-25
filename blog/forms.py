from django import forms
from article.models import *
class Articleform(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','category','content','status']
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model=BlogComment
        fields=['user_name','user_email','content']

        widgets={
            'user_name':forms.TextInput(
                attrs={
                'class':'form-control',
                'placeholder':'Your Name',
                'aria-describedby':'sizing-addon1',
            }),
            'user_email':forms.TextInput(
                attrs={
                'class':'form-control',
                'placeholder':'Your Email',
                'aria-describedby':'sizing-addon1',
            }),
            'content':forms.Textarea(
                attrs={
                    'placeholder':'Comment Some',
                }
            ),
        }
