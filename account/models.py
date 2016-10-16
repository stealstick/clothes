from django.db import models

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=10)
    userid = models.CharField(max_length=30)
    userpw = models.CharField(max_length=30)
    email = models.IntegerField(default=1)
    area_1 = models.CharField(max_length=15)
    area_2 = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name