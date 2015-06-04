from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length=128)

    class Meta:
        db_table = 'message'
