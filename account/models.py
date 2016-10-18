from django.contrib.auth.models import User
from django.db import models

from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User)
    area_1 = models.CharField(max_length=15)
    area_2 = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name