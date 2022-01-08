from django.contrib import admin

from webapp.models import Guest


# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest_name', 'guest_mail', 'created_at']
    list_filter = ['created_at']
    search_fields = ['guest_name']
    fields = [
        'guest_name',
        'guest_mail',
        'guest_text',
        'created_at',
        'updated_at',
        'status'
    ]
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Guest, GuestAdmin)
