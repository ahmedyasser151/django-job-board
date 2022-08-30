from datetime import timezone
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

POST_CATEGORY =(
    ("Health Care","Health Care"),
    ("Inspiration","Inspiration"),
    ("Travel news","Travel news"),
    ("Product","Product"),
    ("Resaurant food","Resaurant food"),
    ("Pharmacy","Pharmacy"),
    ("Computer science","Computer science"),
    ("Modern technology","Modern technology"),
    ("Finance","Finance"),
    ("Others","Others"),
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    # publish = models.DateTimeField(defult=timezone.now())
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=50, choices=POST_CATEGORY)

    class Meta():
        ordering = ['-created_on']


    def __str__(self):
        return self.title
