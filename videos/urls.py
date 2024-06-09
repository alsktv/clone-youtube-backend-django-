from django.urls import path
from .views import Videos,VideoDetail,Reviews,searchVideo

urlpatterns = [
   path("",Videos.as_view()),
   path("<int:pk>",VideoDetail.as_view()),
   path("<int:pk>/reviews",Reviews.as_view()),
   path("result" , searchVideo.as_view())
]