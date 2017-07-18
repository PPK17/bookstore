from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    review = models.TextField(blank=True,null=True)
    date_review = models.DateTimeField(blank=True,null=True)
    is_favourite = models.BooleanField(default=False)