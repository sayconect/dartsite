from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'caterogy'
        verbose_name_plural = 'categories'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

        
class Teg(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Teg, blank=True, related_name='posts')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})