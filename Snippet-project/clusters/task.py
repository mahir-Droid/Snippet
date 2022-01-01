from urllib import request
from celery import shared_task
from time import sleep
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Cluster, Data
from .mycrawler import *
from .models import URL




@shared_task
def createShared(nourl, url_values, depth_values, datatype_values, title, username):

    cluster = Cluster()
    cluster.title = title
    cluster.pub_date = timezone.datetime.now()
    cluster.hunter = User.objects.get(username=username)
    cluster.status = 'unfinished'
    cluster.save()
    print("Cluster Model Created: Status Unfinished")
        
    data_urls_for_this_cluster = []

    for i in range(nourl):
        current_url = url_values[i]
        current_depth = int(depth_values[i])
        current_datatype = datatype_values[i]
        
        user_url_list = geturlswdepth(current_url,current_depth)
                    
        for link in user_url_list:
            
            if(current_datatype == 'text'):
                x = gettext(link)
                if x != None:
                    data_urls_for_this_cluster.append(link)

            elif(current_datatype == 'pdf'):
                x = getpdf(link)
                if x != None:
                    data_urls_for_this_cluster += x

            elif(current_datatype == 'doc'):
                x = getword(link)
                if x != None:
                    data_urls_for_this_cluster += x 

            elif(current_datatype == 'nonhtml'):
                
                x = getpdf(link)
                if x != None:
                    data_urls_for_this_cluster += x
                
                x = getword(link)
                if x != None:
                    data_urls_for_this_cluster += x 

            elif(current_datatype == 'all'):
                x = gettext(link)
                if x != None:
                    data_urls_for_this_cluster.append(link)
                    
                x = getpdf(link)
                if x != None:
                    data_urls_for_this_cluster += x
                
                x = getword(link)
                if x != None:
                    data_urls_for_this_cluster += x

            print("Data Model(s) created for"+str(link))
        
        print("Data Models Created for"+str(i)+"-------")
    
    print(data_urls_for_this_cluster)
    #Adding these data urls in Cluster as reference
    for i in data_urls_for_this_cluster:
        try:
            data_obj = Data.objects.get(data_url=i)
        except:
            continue
        cluster.data.add(data_obj)

    cluster.status = 'finished'
    cluster.save()
    print('------------Cluster Created for '+title+' -------------')




@shared_task
def sleepy(duration, name, test_list):
    #Example code to run in redis server
    cluster = Cluster()
    cluster.title = "Test Model"
    cluster.pub_date = timezone.datetime.now()
    hunter = User.objects.get(username=name) # Usermodel is fetched using the name(str)
    cluster.hunter = hunter
    #cluster.save()
    print("Cluster Model Created")
    print(test_list)
    sleep(duration)
    return None