from django.contrib import admin
from .models import Category

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    
  )
