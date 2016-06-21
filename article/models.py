from django.db import models

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
    category=models.ForeignKey('Category',verbose_name='分類',null=True,blank=True,on_delete=models.SET_NULL)
    create_time=models.DateTimeField('創建時間',auto_now_add=True)
    last_modified_time=models.DateTimeField('修改時間',auto_now=True)
    content=models.TextField('正文',blank=True,null=True)
    status=models.CharField('文章狀態',max_length=1,choices=STATUS_CHOICES)
    abstract=models.CharField('摘要',max_length=30,blank=True,null=True,help_text='空白，則為前30字')
    views=models.PositiveIntegerField('瀏覽量',default=0)
    likes=models.PositiveIntegerField('讚數',default=0)
    topped=models.BooleanField('置頂',default=False)
    def __str__ (self):
        return self.title;
    class Meta:
        ordering=['-last_modified_time'] #from new to old
