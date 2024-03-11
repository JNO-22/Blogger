from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=timezone.now())
    last_modified = models.DateTimeField(auto_now=timezone.now())
    categories = models.ManyToManyField("Category", related_name="posts")
        
    def __str__(self):
        return self.title