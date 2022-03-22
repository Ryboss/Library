from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField('Название',max_length=70)
    image=models.ImageField(upload_to='media/book')
    author=models.CharField('Писатель',max_length=40,default='NoName')