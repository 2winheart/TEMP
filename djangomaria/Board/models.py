from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=10,blank=True)
	title = models.CharField(max_length=20,blank=True)
	created_date = models.DateField(null=True,blank=True)
	memo = models.TextField()

def create(self):
	self.created_date = timezone.now()
	self.save()

def __title__(self):
	return self.title
