from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    notes_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_name = models.CharField(max_length=250)

