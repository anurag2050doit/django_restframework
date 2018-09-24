# Created by anmisra on 9/24/18
from django.conf.urls import url

from spider.views import index

urlpatterns = [
    url(r'^$', index, name='index')
]
