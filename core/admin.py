from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Request, Contact


@admin.register(Request)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message", "timestamp")
    list_display_links = ("name", "email", "phone")
    list_filter = ("timestamp",)
    search_fields = ("name", "email", "phone")
    readonly_fields = ("name", "email", "phone", "message", "timestamp")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "icon")
    list_display_links = ("name", "link")