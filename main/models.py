from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from account.models import User
class Cloth(models.Model):
    cloth_name = models.CharField(max_length=40)
    size = models.CharField(max_length=20)
    category = models.CharField(max_length=20, null=True)
    bo_prize = models.IntegerField(default=1)
    lent_prize = models.IntegerField(default=1)
    cloth_img = models.CharField(max_length=40)
    cloth_intro = models.TextField()
    owner = models.ForeignKey(User, related_name='owner_clother', null=True)
    lenter = models.ForeignKey(User, related_name='lenter_clother', null=True)
    def __str__(self):
        return '%s' % self.cloth_name
