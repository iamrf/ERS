from django.contrib import admin
from . import models

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    # fields = ()
    list_display = ('name', 'location', 'date', 'duration', 'desc', 'created', 'last_modified')
    list_filter = ('date', 'location', 'duration')
    search_fields = ['name', 'location', 'date']
    date_hierarchy = 'date'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'tell', 'address', 'created', 'last_modified')
    list_filter = ('created',)
    search_fields = ('name', 'tell', 'address', 'created')
    date_hierarchy = 'created'
    filter_horizontal = ('event',)


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.User, UserAdmin)
