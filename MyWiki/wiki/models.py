from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.title