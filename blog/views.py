from django.shortcuts import render
from django.http import *
from datetime import datetime
from article.models import *
from django.core.urlresolvers import reverse
from .forms import *
def homepage (request):
    articles=Article.objects.all()
    return render(request,'homepage.html',locals())
def aboutme (request):
    return render(request,'aboutme.html',locals())
def create_article(request):
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        content=request.POST['content']
        Article.objects.create(title=title,content=content)
        return HttpResponseRedirect(reverse('blog.views.homepage'))
    form=Articleform()
    return render(request,'create_article.html',locals())
