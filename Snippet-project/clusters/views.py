from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.dsebd.org/")
soup = BeautifulSoup(r.content, 'html.parser')

headings = soup.find_all()

data = []

for th in headings:
    data.append(th.text)





def home(request):
    return render(request, 'clusters/home.html', {'data':data})
    
