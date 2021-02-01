from django.db import models

class User(models.Model):
	email = models.EmailField(max_length=30, blank=False, primary_key=True)

