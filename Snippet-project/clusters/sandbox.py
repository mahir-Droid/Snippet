
from .models import Cluster, Data
from .mycrawler import *
from .models import URL



urlModel1 = URL()
urlModel1.name = "https://www.youtube.com/watch?v=BFH-IfTB47E"
urlModel1.scraped_date = timezone.now()
urlModel1.save()

urlModel2 = URL(name="https://www.youtube.com/")
urlModel3 = URL(name="https://classroom.google.com/u/0/h")

urlModel2.save()
urlModel3.save()

urlModel1.neighbours.add(urlModel2)
urlModel1.neighbours.add(urlModel3)

