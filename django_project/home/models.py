from email import message
from posixpath import supports_unicode_filenames
from unicodedata import name
from django.db import models
from pyparsing import nestedExpr

class Contact(models.Model):
    name=models.CharField(max_length=122)
    surname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    need=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()