from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from users.models import Profile


@admin.register(Profile)
class BrandsAdmin(SimpleHistoryAdmin):
    list_display = ('user', 'birth_date', 'photo',)

