from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'company', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'company', 'subject', 'message', 'created_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'created_at')
        }),
        ('Management', {
            'fields': ('status', 'notes')
        }),
    )
