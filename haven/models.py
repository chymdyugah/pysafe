from django.db import models
from django.conf import settings

# Create your models here.


class Key(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	pin = models.CharField(max_length=255)
	decrypt_key = models.TextField()


class Platform(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	url = models.URLField()
	username = models.CharField(max_length=255)
	password = models.TextField()
