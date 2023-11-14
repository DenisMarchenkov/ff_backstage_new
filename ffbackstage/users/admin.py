from django.contrib import admin
from django.utils.safestring import mark_safe
from simple_history.admin import SimpleHistoryAdmin

from users.models import Profile


@admin.register(Profile)
class BrandsAdmin(SimpleHistoryAdmin):
    list_display = ('profile_photo', 'user', 'birth_date', )
    list_display_links = ('user',)

    @admin.display()
    def profile_photo(self, profile: Profile):
        if profile.photo:
            return mark_safe(f"<img src='{profile.photo.url}' width=50 height=50>")
        return 'Без фото'
