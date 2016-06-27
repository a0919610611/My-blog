from django.conf.urls import *
from . import views
urlpatterns = [
    url(r'^$',views.ArticleListView.as_view(),name='article_list'),
    url(r'^(?P<article_id>\d+)/$',views.ArticleDetailView.as_view(),name='detail'),
    url(r'^publish/(?P<article_id>\d+)/$',views.publish,name='publish'),
    url(r'^unpublish/(?P<article_id>\d+)/$',views.unpublish,name='unpublish'),
    url(r'^drafts/$', views.article_draft_list, name='article_draft_list'),
    url(r'^admin_article_list/$', views.admin_article_list, name='admin_article_list'),
    url(r'^(?P<article_id>\d+)/comment/$', views.CommentPostView.as_view(), name='comment'),
    url(r'^category/(?P<category_id>\d+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
]
