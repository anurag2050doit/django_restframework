# Created by anmisra on 9/21/18


from django.db import models


class Photos(models.Model):
    dateuploaded = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=500)
    description = models.TextField()
    tags = models.ForeignKey('Tags')
    urls = models.ForeignKey('Urls')
    media = models.CharField(max_length=50)


class Urls(models.Model):
    photo_type = models.CharField(max_length=50)
    content = models.URLField


class Group(models.Model):
    user = models.ManyToManyField('auth.User')
    title = models.TextField(max_length=200)
    photo = models.ForeignKey('Photos', on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    author = models.ForeignKey('auth.User')
    content = models.CharField(max_length=500)
