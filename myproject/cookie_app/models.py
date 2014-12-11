from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from datetime import datetime

##this is a hacky way to get inline forms--see http://lightbird.net/dbe/todo_list.html
class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return unicode(self.datetime)
######################################

class barebones_CRUD(models.Model):
    name = models.CharField(max_length=150, default='0000000')
    BorrName = models.CharField(max_length=150, default='0000001')
    BorrStreet = models.CharField(max_length=150, default='0000002')
    BorrState = models.CharField(max_length=150, default='0000003')
    BorrCity = models.CharField(max_length=150, default='0000004')
    BorrZip = models.CharField(max_length=15, default='0000005')
    Created = models.ForeignKey(DateTime, null=True)
    FollowUp = models.BooleanField(default=False, verbose_name = "Contact Business?")
    FindMoreData = models.BooleanField(default=False, verbose_name = "Find More Information on Business?")
    def __str__(self):
        return self.BorrName
    def get_absolute_url(self):
        return reverse('barebones_crud_detail', args=[str(self.id)])
