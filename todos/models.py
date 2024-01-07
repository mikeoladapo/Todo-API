from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 20)
    about = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
