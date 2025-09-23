from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSetting, Service, Portfolio, TeamMember, 
    Testimonial, FAQ, ContactMessage, Subscriber
)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'logo_preview')
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'logo')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url')
        }),
        ('Content', {
            'fields': ('hero_title', 'hero_description', 'footer_text')
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>'.format(obj.logo.url))
        return "No Logo"
    logo_preview.short_description = 'Logo Preview'

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'display_order', 'is_active', 'image_preview')
    list_editable = ('display_order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>'.format(obj.image.url))
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'image_preview')
    list_editable = ('is_featured',)
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>'.format(obj.image.url))
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_order', 'is_active', 'image_preview')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name', 'position')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>'.format(obj.image.url))
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'created_at')
    search_fields = ('client_name', 'company')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question', 'answer')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'received_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'received_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'received_at')

    def has_add_permission(self, request):
        return False

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'subscribed_at')
    readonly_fields = ('email', 'subscribed_at')

    def has_add_permission(self, request):
        return False

# Customize admin interface
admin.site.site_header = "SoftNext Administration"
admin.site.site_title = "SoftNext Admin Portal"
admin.site.index_title = "Welcome to SoftNext Admin Dashboard"