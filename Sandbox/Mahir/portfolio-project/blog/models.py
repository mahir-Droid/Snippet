from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_nice(self):
        return self.pub_date.strftime('%b %e %Y')

    


#title
#pub_date
#body
#image



#Add the Blog app to the settings


#Create a migrations

#Migrate

#Add to the admin