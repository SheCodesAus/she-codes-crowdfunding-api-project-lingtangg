from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  main_language = models.CharField(max_length=100)
  secondary_language = models.CharField(max_length=100)
  time_required = models.IntegerField()
  location = models.CharField(max_length=100)
  image = models.URLField()
  is_open = models.BooleanField()
  date_created = models.DateTimeField()
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='owner_projects'
  )

class Pledge(models.Model):
  time_pledged = models.IntegerField()
  comment = models.CharField(max_length=200)
  date_created = models.DateTimeField()
  project = models.ForeignKey(
    'Project',
    on_delete=models.CASCADE,
    related_name='pledges')
  supporter = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='supporter_pledges'
  )