from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Job, Volunteer, Client

class JobAdmin(admin.ModelAdmin):
    list_display = ('Volunteer', 'Client', 'Date', 'Summary', 'Location')
    search_fields = ('Volunteer', 'Client', 'Date', 'Summary', 'Location')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Phone', 'Email')
    search_fields = ('First_Name', 'Last_Name', 'Phone', 'Email')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Phone', 'Email', 'Notes')
    search_fields = ('First_Name', 'Last_Name', 'Phone', 'Email', 'Notes')

admin.site.register(Job, JobAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Client, ClientAdmin)
