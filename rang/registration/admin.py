from django.contrib import admin

from . import models

class ParticipantAdmin(admin.ModelAdmin):
    fields = ['name','district','category',]
    search_fields = ['name',]
    list_filter = ['district','category',]
    list_display = ['name','district','category',]

admin.site.register(models.Participant,ParticipantAdmin)