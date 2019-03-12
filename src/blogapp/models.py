from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title       = models.CharField(max_length = 25)
    content     = models.TextField(max_length = 350)
    image       = models.ImageField(upload_to='images/',null=True,blank=True)
    author      = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
