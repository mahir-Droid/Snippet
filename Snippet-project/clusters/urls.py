from django.urls import path, include
from . import views

 
urlpatterns = [
    path('urlprompt/', views.urlprompt, name='urlprompt'),
    path('create/', views.create, name='create'),

]
