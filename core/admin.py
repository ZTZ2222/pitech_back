from django.contrib import admin

from .models import Request


@admin.register(Request)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message", "timestamp")
    list_display_links = ("name", "email", "phone")
    list_filter = ("timestamp",)
    search_fields = ("name", "email", "phone")
    readonly_fields = ("name", "email", "phone", "message", "timestamp")
