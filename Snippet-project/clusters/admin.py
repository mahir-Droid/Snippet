from django.contrib import admin
from .models import URL, Cluster, Data


admin.site.register(Cluster)
admin.site.register(URL)
admin.site.register(Data)
