from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField("Author", related_name="books")
    review = models.TextField(blank=True,null=True)
    date_review = models.DateTimeField(blank=True,null=True)
    is_favourite = models.BooleanField(default=False,verbose_name='Favorite')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=150,help_text="Ingrese nombre del autor")

    def __str__(self):
        return self.name