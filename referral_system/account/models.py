from django.db import models


class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    auth_code = models.CharField(max_length=4)
    invite_code = models.CharField(max_length=6, null=True, blank=True)
    activated_invite_code = models.BooleanField(default=False)


    def __str__(self):
        return self.phone_number


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InviteCodeRelation(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitations_sent')
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitations_received')
    # created_at = models.DateTimeField(auto_now_add=True)