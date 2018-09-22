# Created by anmisra on 9/22/18

from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
from django.contrib.auth.models import User

from services import models

from spider.models import ApiKeys
from pytz import UTC
from spider.get_data import FetchData


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from Flickr into our models"

    def handle(self, *args, **options):
        group_response = None
        api_data_set = ApiKeys.objects.all()
        for api in api_data_set:
            if api.working:
                group_response = self.get_response(api)
        if group_response:
            user = User.objects.get(first_name='Guest')
            group = models.Group.objects.get(id=1)
            for photo in group_response.get('photos', {}).get('photo', []):
                photo_id = photo.get('id')
                if photo_id:
                    print 'Loading data for photoID %s' % photo_id
                    response = self.get_response(api, photo_id=photo_id)
                    if response:
                        # Loading of Photo
                        photo_response = response.get('photo', {})
                        photo = models.Photos()
                        photo.owner = user
                        photo.title = photo_response.get('title', {}).get(
                            '_content')
                        photo.description = photo_response.get(
                            'description').get('_content')
                        photo.urls = self.get_photo_url(
                            photo_response.get('urls'))
                        photo.media = photo_response.get('media')
                        photo.group = group
                        photo.save()

                        # Loading of tags
                        for tag_response in photo_response.get(
                                'tags', {}).get('tag'):
                            content = tag_response.get('raw')
                            print('Loading TagID %s' % tag_response.get('id'))
                            if content:
                                tag = models.Tags()
                                tag.content = tag_response.get('raw')
                                tag.author = user
                                tag.photo = photo
                                tag.save()

    @staticmethod
    def get_response(api, photo_id=None):
        return FetchData(
            api_key=api.api_key, group_url=api.group_url,
            group_id=api.group_id, photo_url=api.photo_url,
            photo_id=photo_id
        ).get()

    @staticmethod
    def get_photo_url(urls):
        if urls and urls.get('url'):
            return urls.get('url')[0].get('_content')
