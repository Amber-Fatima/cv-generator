from django.db import models


# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    summary = models.CharField(max_length=3000)
    degree = models.CharField(max_length=1000)
    school = models.CharField(max_length=1000)
    university = models.CharField(max_length=1000)
    work = models.CharField(max_length=1000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
