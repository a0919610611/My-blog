from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login,logout
from datetime import datetime
from article.models import *
from django.core.urlresolvers import reverse
from .forms import *
from django.views.generic import ListView
import markdown2
class HomePageView(ListView):
    template_name="homepage.html"
    context_object_name="article_list"
    def get_queryset(self):
        article_list=Article.objects.filter(status='p')
        for article in article_list:
            article.content=markdown2.markdown(article.content, extras=['fenced-code-blocks'],)
        return article_list
    def get_context_data(self,**kwargs):
        kwargs['category_list']=Category.objects.all().order_by('name')
        return super(HomePageView,self).get_context_data(**kwargs)
def homepage (request):
    articles=Article.objects.all()
    return render(request,'homepage.html',locals())
def aboutme (request):
    return render(request,'aboutme.html',locals())
def create_article(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        content=request.POST['content']
        status=request.POST['status']
        Article.objects.create(title=title,content=content,status=status)
        return HttpResponseRedirect('/')
    form=Articleform()
    return render(request,'create_article.html',locals())
def edit_article(request,article_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    article=Article.objects.get(pk=article_id)
    if request.method=='POST':
        form=Articleform(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form=Articleform(instance=article)
    return render(request,'edit_article.html',locals())
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
