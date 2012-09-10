from django.db import models


class Project(models.Model):
    github_url = models.URLField(unique=True)
    channel_token = models.CharField(max_length=255)

    def __unicode__(self):
        return self.github_url


class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    grove_nick = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
