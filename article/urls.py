from django.conf.urls import *
from . import views
urlpatterns = [
    url(r'^$',views.article_list,name='article_list'),
    url(r'^(?P<article_id>\d+)/$',views.ArticleDetailView.as_view(),name='detail'),
]
