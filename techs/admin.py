from django.contrib import admin

from techs.models import Tech


class TechAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'tags']}),
    ]
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Tech, TechAdmin)
