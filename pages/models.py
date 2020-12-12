from django.db import models


class LeaderProfile(models.Model):
    name = models.CharField(max_length=60, blank=False)
    position = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True, null=False)
    profile_image = models.ImageField(upload_to='staticfiles/images/', blank=False, null=True)


class DoulosProfile(models.Model):
    name = models.CharField(max_length=60, blank=False)
    position = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True, null=False)
    profile_image = models.ImageField(upload_to='staticfiles/images/', blank=False, null=True)


class MenStudy(models.Model):
    date = models.CharField(max_length=25, blank=False)
    location = models.CharField(blank=False, max_length=50)


class WomenStudy(models.Model):
    date = models.CharField(max_length=25, blank=False)
    location = models.CharField(blank=False, max_length=50)


class Event(models.Model):
    title = models.CharField(blank=False, max_length=50)
    date = models.CharField(max_length=25, blank=False)
    location = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=True, null=False)