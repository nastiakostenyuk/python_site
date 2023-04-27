from django.db import models

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:category', kwargs={'parameter': self.name})


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:article', kwargs={'article_id': self.pk})

