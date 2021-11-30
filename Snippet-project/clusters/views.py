from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Cluster
from .models import URL

from .mycrawler import *





def welcome(request):
    return render(request, 'clusters/welcome.html')





@login_required
def urlprompt(request):
    if request.method == 'GET':
        return render(request, 'clusters/urlprompt.html')
    elif request.method == 'POST':    
        title = request.POST['title']
        nourl = request.POST['nourl']
        n = nourl
        nourl = range(int(nourl))
        errors = []
        return render(request, 'clusters/create.html', {'title':title,'n':n, 'nourl':nourl, 'errors':errors})





@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'clusters/create.html')
    if request.method == 'POST':

        cluster = Cluster()
        cluster.title = request.POST['title']
        cluster.pub_date = timezone.datetime.now()
        cluster.hunter = request.user
        cluster.save()
        print("Cluster Model Created")

        
        nourl = request.POST['n']
        nourl = int(nourl)
        url_values = request.POST.getlist('url')
        depth_values = request.POST.getlist('depth')


        for i in range(nourl):
            current_url = url_values[i]
            current_depth = int(depth_values[i])
            
            user_url_list = geturlswdepth(current_url,current_depth)
            
            for link in user_url_list:
                url_model = URL()
                url_model.hunter = request.user
                url_model.cluster = cluster
                url_model.urlname = link
                
                textlist = gettext(link)
                textdata = " ".join(textlist)
                
                url_model.text_data = textdata 
                url_model.save()
                print("URL Model Created for"+str(link))
            
            print("URL Models Created for"+str(i)+"-------")

        return redirect('home')
