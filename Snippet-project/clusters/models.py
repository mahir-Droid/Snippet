from django.db import models
from django.contrib.auth.models import User

class Cluster(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class URL(models.Model):
    urlname = models.CharField(max_length=500)
    text_data = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return self.urlname    

    def summary(self):
        self.text_data[:100]