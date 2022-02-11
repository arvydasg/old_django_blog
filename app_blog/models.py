from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateField(auto_now=False)

    class Meta:
        ordering = ['-date_added']
