from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Royxat(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True)
    category = models.ForeignKey(to=Category , on_delete=models.CASCADE, related_name="Royxat")
    SHIRT_SIZES = [
        ("H","High"),
        ("L","Low"),
        ("M","Middle"),
    ]
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title

      
