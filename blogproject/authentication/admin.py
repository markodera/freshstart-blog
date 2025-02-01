from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    def profile_picture_display(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%; object-fit:cover;" />', obj.profile_picture.url)
        return "No Image"
    
    profile_picture_display.short_description = 'Profile Picture'
    
    list_display = ('username', 'email', 'profile_picture_display')
    list_display_links = ('username', 'profile_picture_display')
    search_fields = ('username', 'email')
    readonly_fields = ('profile_picture_display',)

admin.site.register(CustomUser, CustomUserAdmin)