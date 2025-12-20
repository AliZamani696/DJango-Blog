from django.contrib.auth.models import update_last_login
from django.db import models
from Accounts.models import CustomUser


# Create your models here.



class Post(models.Model):
    author= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/posts/images")
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=150)
    status = models.BooleanField(default=False)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
