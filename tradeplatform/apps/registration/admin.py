from django.contrib import admin

from apps.registration.models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "is_valid", "date_joined")
    list_filter = ("is_valid",)
    search_fields = (
        "user__username",
        "user__email",
    )
    ordering = (
        "user__username",
        "user__email",
    )
