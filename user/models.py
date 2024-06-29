from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class Group(models.Model):
    # fields
    user_set = models.ManyToManyField(User, related_name='custom_group_users')

class Permission(models.Model):
    # fields
    user_set = models.ManyToManyField(User, related_name='custom_permission_users')