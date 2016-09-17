from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class lazy_links(models.Model):
    user= models.ForeignKey(User)
    created= models.DateTimeField(auto_now=True)
    key= models.CharField(max_length=150)

    def __str__(self):
        return "{}-{}".format(self.user.username, self.created)

    class Meta:
        ordering = ['created']
