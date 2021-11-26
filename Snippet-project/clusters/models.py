from django.db import models
from django.contrib.auth.models import User

class Cluster(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text_data = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title