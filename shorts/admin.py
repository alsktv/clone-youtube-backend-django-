from django.contrib import admin
from .models import Shorts

@admin.register(Shorts)
class ShortsAdmin(admin.ModelAdmin):
  list_display = [
    "name",
    "user",
    "created_at",
 
  ]