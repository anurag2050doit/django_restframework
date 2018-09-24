# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from services import serializers
from services.models import Group, Photos


class GroupViewSet(generics.ListAPIView):
    serializer_class = serializers.GroupUserSerializer
    authentication_classes = [JSONWebTokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(user=user.pk)


class GroupDetailViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = serializers.GroupPhotoSerializer
    queryset = Group.objects.all()


class PhotoDetailViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = serializers.PhotoDetailSerializer
    queryset = Photos.objects.all()
