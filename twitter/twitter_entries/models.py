from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.content


