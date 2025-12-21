from operator import pos
from unicodedata import category
from django.contrib import auth
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.utils.text import TruncateHTMLParser
from .models import Category,Post
from Accounts.models import CustomUser
import tempfile
from PIL import Image
import os
# Create your tests here.



def create_test_image():
    image = Image.new("RGB",(100,100),color="red")
    temp_file = tempfile.NamedTemporaryFile(suffix=".png",delete=False)
    temp_file.seek(0)
    uploaded_file = SimpleUploadedFile(
        name="test_image.png",
        content=temp_file.read(),
        content_type="image/png"
    )
    temp_file.close()
    os.unlink(temp_file.name)
    return uploaded_file



class CategoryModelTests(TestCase):
    def setUp(self):
        self.sample_category_name = "Technolgy"
        self.sample_category = Category.objects.create(
            category = self.sample_category_name
        )

    def test_create_category_successful(self):
        category_name = "Science"
        category = Category.objects.create(
            category=category_name
        )
        self.assertEqual(category.category,category_name)
        self.assertIsNotNone(category.id)
        self.assertIsNotNone(category.pk)
        category_from_db = Category.objects.get(id=category.id)
        self.assertEqual(category_from_db.category,category_name)





class PsotModelTests(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.CreateUser(
            email = "test@gmail.com",
            password = "2343234"
        )
        self.test_category = Category.objects.create(
            category = "test category"
        )
        self.another_category =  Category.objects.create(
            category = "another category"
        )
        self.test_image = create_test_image()
        self.valid_post_data = {
            "auther": self.test_user,
            "image" : self.test_image,
            "title" : "test tilte",
            "content": "test content",
            "status" : True,
            "category":self.test_category
        }

    def test_create_post_successful(self):
        post = Post.objects.create(
            author=self.test_user,
            image = self.test_image,
            title = "title 1",
            content = "content 1",
            status = True,
            category = self.test_category
            )
        self.assertIsNotNone(post.author,self.test_user)
        self.assertEqual(post.category,self.test_category)
        self.assertEqual(post.title ,"title 1")
