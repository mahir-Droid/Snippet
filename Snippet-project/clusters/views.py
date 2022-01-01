from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Cluster
from .models import URL, Data
from django.http import HttpResponse

from .mycrawler import *
from .task import *

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.contrib.postgres.search import SearchHeadline

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
        
        username = request.user.username
        title = request.POST['title']

        nourl = request.POST['n']
        nourl = int(nourl)
        url_values = request.POST.getlist('url')
        depth_values = request.POST.getlist('depth')
        datatype_values = request.POST.getlist('datatype')

        print(nourl)
        print(url_values)
        print(depth_values)
        print(datatype_values)
        
        createShared.delay(nourl, url_values, depth_values, datatype_values, title, username)

        return redirect('home')






@login_required
def search(request):

    q = request.GET.get('q')
    if q:
        vector = SearchVector('data_url', 'content', 'type')
        query = SearchQuery(q)

        search_headline = SearchHeadline('content', query)

        #search_data = Data.objects.filter(data_url__search=q)
        #search_data = Data.objects.annotate(search=vector).filter(search=query)
        #search_data = Data.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.0001).order_by('-rank')
        search_data = Data.objects.annotate(rank=SearchRank(vector, query)).annotate(headline=search_headline).filter(rank__gte=0.0001).order_by('-rank')

    else:
        search_data = None


    context={'search_data': search_data}
    
    return render(request, 'clusters/search.html', context)




#A function for tesing stuff. Use /cluster/test to invoke this function
def test(request):

    #url = "https://file-examples-com.github.io/uploads/2017/02/file-sample_100kB.doc"

    #datalist = testmethod(url)
    #datalist = ' '.join(datalist)

    #Sample for using celery to schedule task to redis server
    name = request.user.username
    test_list = ['f','g','h']  
    #sleepy.delay(10, name, test_list)  #Note that request, model objects cannot be sent to celery as they are not serializable.
    # Only json serialisable objects like int,str etc. can be sent. In this case the particular object(like the username of hunter) required
    # are sent and then the Usermodel is fetched using that name and used in celery task function.
    #return HttpResponse("<h1>Testing.|||</h1>"+ datalist)
    
    #data = gettext("https://example.com")

    Cluster.objects.all().delete()
    Data.objects.all().delete()
    URL.objects.all().delete()
    
    #x = getlinksoffile('https://www.princexml.com/samples/', 'pdf')
    #data = givepdf('http://css4.pub/2015/usenix/example.pdf')
    #data = givedocx('https://file-examples-com.github.io/uploads/2017/02/file-sample_100kB.docx')

    return HttpResponse("Success")


