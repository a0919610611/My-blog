from django.conf.urls import *
from . import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'^(?P<id>\d+)/$',views.detail),
]
