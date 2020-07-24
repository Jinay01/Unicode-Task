from django.db import models

# Create your models here.


class Newnums(models.Model):
    numb1 = models.FloatField(null=True)
    numb2 = models.FloatField(null=True)


class Apiinput(models.Model):
    username = models.CharField(max_length=200, null=True)
    counter = models.FloatField(default=1)
    repo_count = models.FloatField(default=0)
    followers_count = models.FloatField(default=0)
    following_count = models.FloatField(default=0)

    def __str__(self):
        return self.username


# class Usercheck(models.Model):
#     usercheck = models.CharField(max_length=200, null=True)
