from django.contrib import admin
from .models import *
# Register your models here.
#class ArticleAdmin(admin.ModelAdmin):

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Photo)
