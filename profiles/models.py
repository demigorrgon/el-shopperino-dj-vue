from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.user.username


def create_profile_when_user_created(sender, instance, *args, **kwargs):
    if instance:
        Profile.objects.get_or_create(user=instance)


def delete_profile_when_user_deleted(sender, instance, *args, **kwargs):
    if instance:
        user = Profile.objects.get(user=instance)
        user.delete()


post_save.connect(create_profile_when_user_created, sender=User)
post_delete.connect(delete_profile_when_user_deleted, sender=User)
