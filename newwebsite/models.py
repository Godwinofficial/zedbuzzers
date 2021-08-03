from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.


class Category(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(null=True, unique=True)
  
  def __str__(self):
    return self.title



class Post(models.Model):
  image       = models.ImageField(upload_to='images/')
  file        = models.FileField(null=True, upload_to='files/')
  name        = models.CharField(blank=True, max_length=100)
  title       = models.CharField(max_length=100, blank=True)
  category    = models.ForeignKey(Category, on_delete=CASCADE)
  time_stamp  = models.DateTimeField(auto_created=True)
  posted_by   = models.CharField( max_length=30, default='Godwin')
  description = models.TextField(max_length=5000)
  post_views  = models.IntegerField(default=0)
  slug        = models.SlugField(null=True, unique=True)

  def __str__(self):
    return self.name



  def get_absolute_url(self, *args, **kwargs):
    return reverse('post-details', kwargs={'slug': self.slug})