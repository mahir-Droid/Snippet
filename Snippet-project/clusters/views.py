from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'clusters/welcome.html')

@login_required
def urlprompt(request):
    if request.method == 'GET':
        return render(request, 'clusters/urlprompt.html')
    elif request.method == 'POST':    
        title = request.POST['title']
        nourl = request.POST['nourl']
        nourl = range(int(nourl))
        return render(request, 'clusters/create.html', {'title':title, 'nourl':nourl})

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'clusters/create.html')
    if request.method == 'POST':
    #TODO: scrape data from urls recursively and
    # save them in the database or a filemanagement system
    # with the username of the user logged in.
    # Create a tree structured storage where data is stored
    # in reference to the url that has them
    # finally redirect user to the home page.  
        return redirect('create')
