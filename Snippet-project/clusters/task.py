from urllib import request
from celery import shared_task
from time import sleep
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Cluster


@shared_task
def sleepy(duration, name):
    #Example code to run in redis server
    cluster = Cluster()
    cluster.title = "Test Model"
    cluster.pub_date = timezone.datetime.now()
    hunter = User.objects.get(username=name) # Usermodel is fetched using the name(str)
    cluster.hunter = hunter
    cluster.save()
    print("Cluster Model Created")

    sleep(duration)
    return None