from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
    age = models.PositiveBigIntegerField()
    def __str__(self):
        return str(self.name)