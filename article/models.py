from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField('類名',max_length=50,blank=True)
    create_time=models.DateTimeField('創建時間',auto_now_add=True)
    last_modified_time=models.DateTimeField('修改時間',auto_now=True)
    def __str__(self):
        return  self.name
class Article (models.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Published'),
    )
    title=models.CharField('標題',max_length=100)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,verbose_name='分類',null=True,blank=True)
    create_time=models.DateTimeField('創建時間',auto_now_add=True)
    last_modified_time=models.DateTimeField('修改時間',auto_now=True)
    content=models.TextField('正文',blank=True,null=True)
    status=models.CharField('文章狀態',max_length=1,choices=STATUS_CHOICES,default='d')
    abstract=models.CharField('摘要',max_length=30,blank=True,null=True,help_text='空白，則為前30字')
    views=models.PositiveIntegerField('瀏覽量',default=0)
    likes=models.PositiveIntegerField('讚數',default=0)
    topped=models.BooleanField('置頂',default=False)
    def get_absolute_url(self):
        return reverse('article:detail',kwargs={'article_id':self.pk})
    def publish(self):
        self.status='p'
        self.save()
    def unpublish(self):
        self.status='d'
        self.save()
    def is_published(self):
        return self.status=='p'
    def __str__ (self):
        return self.title;
    class Meta:
        ordering=['-last_modified_time'] #from new to old
class BlogComment(models.Model):
    user_name=models.CharField('Name',max_length=100)
    user_email=models.EmailField('Email',max_length=255)
    content=models.TextField('Content')
    create_time=models.DateTimeField('Created Time',auto_now_add=True)
    article=models.ForeignKey('Article',on_delete=models.CASCADE,verbose_name='Commented Article')
    def __str__(self):
        return self.content[:20]
