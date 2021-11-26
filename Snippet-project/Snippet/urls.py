from django.contrib import admin
from django.urls import path, include
from clusters import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('accounts/', include('accounts.urls')),
    path('clusters/', include('clusters.urls')),

]
