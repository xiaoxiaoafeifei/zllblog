from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=False)
    published_time = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return self.title
