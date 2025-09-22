from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSetting   # ← make sure this line exists


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="100"/>'.format(obj.logo.url))
