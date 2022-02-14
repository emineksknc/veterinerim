# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class Pet(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Hayvan Sahibi', related_name='pets')
    type = models.CharField(max_length=120, verbose_name="Tür")
    breed = models.CharField(max_length=120, verbose_name="Cins")
    name = models.CharField(max_length=60, verbose_name="Ad")
    age = models.PositiveIntegerField(verbose_name="Yaş")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('pet:detail', kwargs={'id': self.id})

    def get_create_url():
        return reverse('pet:create')

    def get_update_url(self):
        return reverse('pet:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('pet:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-id']
