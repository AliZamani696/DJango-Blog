from django.db import models
from accounts.models import User
from django.conf import settings
# Create your models here.


class Post(models.Model):
    ''''
        this is class for blog post model
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    categrory = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/',null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
