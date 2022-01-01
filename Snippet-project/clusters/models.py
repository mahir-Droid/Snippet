from django.db import models
from django.contrib.auth.models import User

class Cluster(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Incomplete')
    data = models.ManyToManyField('Data', null=True)

    def __str__(self):
        return self.title



class URL(models.Model):
    name = models.CharField(max_length=500)
    neighbours = models.ManyToManyField('self', blank=True, null=True, symmetrical=False)
    scraped_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name

class Data(models.Model):
    data_url = models.CharField(max_length=500)
    url = models.ManyToManyField(URL, null=True)
    type = models.CharField(max_length=10)
    content = models.TextField()

    scraped_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.data_url    

    def summary(self):
        self.content[:100]
