from django.contrib import admin
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'code')
    