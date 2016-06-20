from django.conf.urls import *
from . import views
urlpatterns = [
    url(r'^$',views.article_list,name='article_list'),
    url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
]
