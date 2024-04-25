from django.db import models


class User(models.Model):
    phone_number = models.CharField(unique=True)
    password = models.CharField()
    invite_code = models.CharField(default=None)
    invited_by = models.CharField(default=None, null=True)

    def __str__(self):
        return self.phone_number


class Invitation(models.Model):
    inviter = models.ForeignKey(User, related_name='invitations_sent', on_delete=models.CASCADE)
    invitee = models.ForeignKey(User, related_name='invitations_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inviter.phone_number} invited {self.invitee.phone_number}"

