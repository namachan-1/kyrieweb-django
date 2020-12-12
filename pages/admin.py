from django.contrib import admin
from .models import LeaderProfile, DoulosProfile, MenStudy, WomenStudy, Event


class LeaderProfileAdmin(admin.ModelAdmin):
   list_display = ('name', 'position')

class DoulosProfileAdmin(admin.ModelAdmin):
   list_display = ('name', 'position')

class MenStudyAdmin(admin.ModelAdmin):
   list_display = ('date', 'location')

class WomenStudyAdmin(admin.ModelAdmin):
   list_display = ('date', 'location')

class EventAdmin(admin.ModelAdmin):
   list_display = ('title', 'date', 'location')



admin.site.register(LeaderProfile, LeaderProfileAdmin)
admin.site.register(DoulosProfile, DoulosProfileAdmin)
admin.site.register(MenStudy, MenStudyAdmin)
admin.site.register(WomenStudy, WomenStudyAdmin)
admin.site.register(Event, EventAdmin)

