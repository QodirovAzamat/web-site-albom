from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        db_table = "categories"

class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "tags"


class Post(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="posts/%Y/%m/%d")
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="posta")
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "posts"