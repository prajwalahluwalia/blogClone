from django.db import models
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=500)
    skills = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('cvGen:all')