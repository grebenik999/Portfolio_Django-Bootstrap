from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.title

    def timestamp_pretty(self):
        return self.timestamp.strftime('%b %e %Y')
