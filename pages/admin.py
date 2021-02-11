from django.contrib import admin
from .models import team
from django.utils.html import format_html
# Register your models here.

class teamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "40px" style = "border-radius: 50px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'photo'
        

    list_display = ("id","thumbnail","first_name","designation","created_date")
    list_display_links = ("id","first_name",)
    list_filter = ("designation",)

admin.site.register(team, teamAdmin)
