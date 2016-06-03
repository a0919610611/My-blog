from django.shortcuts import render
from django.http import *
from models import *
from datetime import datetime

# Create your views here.
def home(request):
    articles=Article.objects.all()
    return render(request,'article_list.html',locals())
def detail(request,id):
    try:
        post=Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'detail.html',locals())
