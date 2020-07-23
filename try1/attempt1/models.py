from django.db import models

# Create your models here.


class Newnums(models.Model):
    numb1 = models.FloatField(null=True)
    numb2 = models.FloatField(null=True)


class Apiinput(models.Model):
    username = models.CharField(max_length=200, null=True)
