from django.contrib import admin

from . import models

class ParticipationInLine( admin.TabularInline):
    model = models.Paricipation
    max_num = 5
    min_num = 0
class ParticipantAdmin(admin.ModelAdmin):
    fields = ['name','district','category','phone']
    search_fields = ['name',]
    list_filter = ['district','category',]
    list_display = ['name','district','category','phone']
    inlines = [ParticipationInLine]

class EventInLine( admin.TabularInline):
    model = models.Paricipation
    max_num = 0
    ordering = ("-score",)
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False
class EventAdmin(admin.ModelAdmin):
    inlines = [EventInLine]


admin.site.register(models.Participant,ParticipantAdmin)
admin.site.register(models.Event , EventAdmin)