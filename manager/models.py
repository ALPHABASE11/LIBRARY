from django.db import models

# Create your models here.

class admininfo(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True,unique=True)
    password=models.CharField(max_length=30)

class book(models.Model):
    subject=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    author=models.CharField(max_length=50,null=True)
    publisher=models.CharField(max_length=50,null=True)
    edition_no=models.IntegerField(null=True)
    number_of_pages=models.IntegerField(null=True)
    shelf_no=models.IntegerField(null=True)
    date = models.DateTimeField(null=True)