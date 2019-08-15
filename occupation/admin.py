from django.contrib import admin

from .models import Occupation


class BdAdmin(admin.ModelAdmin):
    list_display = ('name','company_name','position_name','hireDate','fireDate','salary','fraction', 'base','advance','by_hours')
    list_display_links = ('name','position_name')
    search_fields = ('name','position_name')

admin.site.register(Occupation,BdAdmin)