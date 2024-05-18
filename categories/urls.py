from django.urls import path
from .views import Categories

urlpatterns = [
  path("",Categories.as_view())
]