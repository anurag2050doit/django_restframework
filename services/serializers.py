# Created by anmisra on 9/23/18
from rest_framework import serializers

from services.models import Group, Photos, Tags


class GroupUserSerializer(serializers.ModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    photos_count = serializers.IntegerField(source='photos.count',
                                            read_only=True)
    created = serializers.DateTimeField(format='%s')

    class Meta:
        model = Group
        fields = [
            'pk',
            'user',
            'created',
            'title',
            'description',
            'photos',
            'photos_count'
        ]

    @staticmethod
    def get_photos(obj):
        return obj.photo_set.count()


class TagsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = [
            'author',
            'content'
        ]


class PhotoDetailSerializer(serializers.ModelSerializer):
    tags = TagsDetailSerializer(many=True, read_only=True)
    dateuploaded = serializers.DateTimeField(format='%s')

    class Meta:
        model = Photos
        fields = [
            'dateuploaded',
            'owner',
            'title',
            'description',
            'urls',
            'media',
            'group',
            'tags',
        ]


class GroupPhotoSerializer(serializers.ModelSerializer):
    photos = PhotoDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = [
            'photos'
        ]
