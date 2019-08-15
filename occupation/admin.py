from django.contrib import admin

from .models import Occupation


class BdAdmin(admin.ModelAdmin):
    list_display = ('name','companyName','positionName','hireDate','fireDate','salary','fraction', 'base','advance','by_hours')
    list_display_links = ('name','positionName')
    search_fields = ('name','positionName')

admin.site.register(Occupation,BdAdmin)