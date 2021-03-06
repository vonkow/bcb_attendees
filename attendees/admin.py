from django.contrib import admin
from barcampboston.attendees.models import *

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ['^first_name', '^last_name', '^twitter', 'affiliation', 'website']
    list_display = ('__unicode__', 'twitter', 'website', 'affiliation', 'eb_id', 'event_names', 'sponsor', 'patron')

admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Event, EventAdmin)

admin.site.register(EventbriteConfig)

admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(Talk)
