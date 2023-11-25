from pyexpat import model
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created__at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
