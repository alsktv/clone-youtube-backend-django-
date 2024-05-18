from django.contrib import admin
from .models import Video

@admin.register(Video)
class videoAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "user",
    "created_at",
  )
