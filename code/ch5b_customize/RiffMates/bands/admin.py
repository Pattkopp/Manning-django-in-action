# RiffMates/bands/admin.py
from django.contrib import admin

from bands.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "show_weekday",
    )

    def show_weekday(self, obj):
        # Fetch weekday of artist's birth
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"
