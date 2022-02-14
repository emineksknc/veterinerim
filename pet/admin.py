# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pet.models import Pet


# Register your models here.

class PetAdmin(admin.ModelAdmin):

    list_display = ['name', 'type', 'breed', 'age']

    list_filter = ['type', 'breed', 'age']
    search_fields = ['name']

    class Meta:
        model = Pet


admin.site.register(Pet, PetAdmin)
