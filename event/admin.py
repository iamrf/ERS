from django.contrib import admin
from . import models

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    # fields = ()
    list_display = ('name', 'location', 'date', 'duration', 'price', 'desc', 'created', 'last_modified')
    list_filter = ('date', 'location', 'duration', 'price')
    search_fields = ['name', 'location', 'date']
    date_hierarchy = 'date'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'tell', 'email', 'age', 'address', 'desc', 'created', 'last_modified')
    list_filter = ('event', 'created')
    search_fields = ('name', 'tell', 'address', 'created', 'desc')
    date_hierarchy = 'created'
    filter_horizontal = ('event',)


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.User, UserAdmin)
