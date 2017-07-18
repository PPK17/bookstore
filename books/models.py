from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100,help_text='Nombre del autor')
    review = models.TextField(blank=True,null=True)
    date_review = models.DateTimeField(blank=True,null=True)
    is_favourite = models.BooleanField(default=False,verbose_name='Favorite')

    def __str__(self):
        return self.title