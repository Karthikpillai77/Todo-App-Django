from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    img = models.ImageField(upload_to = "images/") 
