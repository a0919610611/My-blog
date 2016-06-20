from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return  self.name
class Article (models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,null=True,blank=True)
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=True,null=True)

    def __str__ (self):
        return self.title;
    class Meta:
        ordering=['-date_time'] #from new to old
