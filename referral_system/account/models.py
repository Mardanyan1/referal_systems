from django.db import models


class User(models.Model):
    phone_number = models.CharField(unique=True)
    password = models.CharField()
    invite_code = models.CharField(default=None)
    invited_by = models.CharField(default=None, null=True)

    def __str__(self):
        return self.phone_number

