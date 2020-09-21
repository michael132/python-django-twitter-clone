from django.db import models
from django.conf import settings
import random


User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images', blank=True)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0, 200)
        }

    class Meta:
        ordering = ['-id']