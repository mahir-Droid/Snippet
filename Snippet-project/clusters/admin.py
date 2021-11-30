from django.contrib import admin
from .models import URL, Cluster


admin.site.register(Cluster)
admin.site.register(URL)
