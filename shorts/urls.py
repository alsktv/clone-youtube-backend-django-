from django.urls import path
from .views import shorts

urlpatterns = [
  path("",shorts.as_view()),
]