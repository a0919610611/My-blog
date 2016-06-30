from django import forms
from article.models import *
class Articleform(forms.ModelForm):
    class Meta:
        model=Article
<<<<<<< HEAD
        fields=['title','category','content','abstract','tags','status']
=======
        fields=['title','category','content','abstract','status']
>>>>>>> 59bc364be4d87c77b7a1e8ef39ea48f9d984b2d3
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model=BlogComment
        fields=['user_name','user_email','content']

        widgets={
            'user_name':forms.TextInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'名子',
                 'aria-describedby':'sizing-addon1',
            }),
            'user_email':forms.TextInput(
                attrs={
                'class':'form-control',
                'placeholder':'信箱(非必要，不會顯示)',
                'aria-describedby':'sizing-addon1',
            }),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'想說的話',
                    'aria-describedly':'sizing-addon1'
                }
            ),
        }
