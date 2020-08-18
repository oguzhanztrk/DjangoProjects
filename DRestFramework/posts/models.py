from datetime import timezone

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
CATEGORY_CHOICES = (
    ('DJ','Django'),
    ('R','Ruby'),
)

class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    custom_id = models.IntegerField(default=1)
    category = models.CharField(max_length=3,choices=CATEGORY_CHOICES,default='none')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment')

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title