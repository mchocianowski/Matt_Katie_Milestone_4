from django.db import models
from django.contrib.auth.models import User


class Category_blog(models.Model):

    class Meta:
        verbose_name_plural = 'Category_blog'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    category_blog = models.ForeignKey('Category_blog', null=True,
                                      blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
