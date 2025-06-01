from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "category", "submitted_at")
    list_filter = ("category", "submitted_at")
    search_fields = ("name", "email", "subject", "description")
    readonly_fields = ("submitted_at",)
    ordering = ("-submitted_at",)
