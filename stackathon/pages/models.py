from django.db import models

# Create your models here.
class Data(models.Model):
  username = models.CharField(max_length=100)
  url = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.username
