"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePageView.as_view(),name='homepage'),
    url(r'^aboutme/$',views.aboutme,name='aboutme'),
    url(r'^logout/$',views.log_out,name='logout'),
    url(r'^create_article/$',views.create_article,name='create_article'),
    url(r'^edit_article/(?P<article_id>\d+)/$',views.edit_article,name='edit_article'),
    url(r'^article/',include('article.urls',namespace='article')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
