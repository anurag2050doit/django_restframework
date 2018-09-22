# Created by anmisra on 9/22/18
from urllib import urlencode

import requests


class FetchData(object):
    def __init__(self, *args, **kwargs):
        self.api_key = kwargs['api_key']
        self.group_url = kwargs['group_url']
        self.group_id = kwargs.get('group_id')
        self.photo_url = kwargs.get('photo_url')
        self.photo_id = kwargs.get('photo_id')

    def get(self):
        url = self.get_url()
        response = requests.get(url)
        if response.status_code < 300:
            return response.json()

    def get_url(self):
        query = {'api_key': self.api_key, 'format': 'json',
                 'nojsoncallback': '1'}
        if not self.photo_id:
            query.update({'group_id': self.group_id})
            return self.group_url + '&' + urlencode(query)
        else:
            query.update({'photo_id': self.photo_id})
            return self.photo_url + '&' + urlencode(query)
