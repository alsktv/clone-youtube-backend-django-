from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
  list_display = (
    "user",
    "text",
    "updated_at",
  )
