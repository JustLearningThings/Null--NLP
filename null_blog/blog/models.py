from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=512)
    image = models.ImageField(upload_to='uploads/post/', blank=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=256)
    pub_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='related post', default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', default=0)

    def __str__(self):
        return f'{self.author}\'s comment'
