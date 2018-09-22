# Created by anmisra on 9/21/18


from django.db import models


class Photos(models.Model):
    dateuploaded = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=500)
    description = models.TextField()
    urls = models.URLField()
    media = models.CharField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True)


class Group(models.Model):
    user = models.ManyToManyField('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    description = models.TextField()


class Tags(models.Model):
    author = models.ForeignKey('auth.User')
    content = models.CharField(max_length=500)
    photo = models.ForeignKey('Photos')
