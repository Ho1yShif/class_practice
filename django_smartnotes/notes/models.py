from django.db import models


# Create your models here.
class Notes(models.model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
