from django.urls import path
from .views import Videos,VideoDetail,Reviews

urlpatterns = [
   path("",Videos.as_view()),
   path("<int:pk>",VideoDetail.as_view()),
   path("<int:pk>/reviews",Reviews.as_view()),
]