# Created by anmisra on 9/23/18

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from services.views import GroupDetailViewSet, GroupViewSet, PhotoDetailViewSet

urlpatterns = [
    url(r'^login$', obtain_jwt_token, name='api-login'),
    url(r'^group/$', GroupViewSet.as_view(),
        name='group-rub'),
    url(r'^group/(?P<pk>\d+)$', GroupDetailViewSet.as_view(),
        name='group-detail'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetailViewSet.as_view(),
        name='photo-detail')
]
