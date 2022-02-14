# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('petowner:detail', kwargs={'id': self.id})

    def get_create_url():
        return reverse('petowner:create')

    def get_update_url(self):
        return reverse('petowner:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('petowner:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-id']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
