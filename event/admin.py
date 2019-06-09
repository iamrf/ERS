from django.contrib import admin
from . import models

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    # fields = ('name', 'location')
    list_display = ('name', 'location', 'date', 'duration', 'desc', 'created', 'last_modified')
    list_filter = ('date', 'location', 'duration')
    search_fields = ['name', 'location', 'date']    

admin.site.register(models.Event, EventAdmin)
