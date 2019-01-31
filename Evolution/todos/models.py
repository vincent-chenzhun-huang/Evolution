from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
