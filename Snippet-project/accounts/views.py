from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required



import requests
from bs4 import BeautifulSoup



@login_required
def home(request):    
    #TODO: Delete the code below. 
    # get all the clusternames and list them
    # with radio buttons with submit buttons named
    # search. Then direct to the search page. 
    r = requests.get("https://www.dsebd.org/")
    soup = BeautifulSoup(r.content, 'html.parser')

    headings = soup.find_all()

    data = []

    for th in headings:
        data.append(th.text)

    return render(request, 'accounts/home.html', {'data':data})
    



def signup(request):
    if request.method == 'POST':
        #user wants to signup
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already exists.Try another.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password does not match.'})
    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username/Password combination is not correct.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

