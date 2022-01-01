from django.urls import path, include
from . import views

 
urlpatterns = [
    path('urlprompt/', views.urlprompt, name='urlprompt'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('test/',views.test, name='test')
]
