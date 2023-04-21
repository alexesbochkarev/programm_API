from django.contrib import admin
from .models import Program, NewsModel, InstructionModel


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'code')


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title', 'text')


@admin.register(InstructionModel)
class InstructionModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'site')
    