from django.urls import path
from .views import UserDetail,CreateUser,logIn,logOut,JWTLogIn

urlpatterns = [
  path("<int:pk>",UserDetail.as_view()),
  path("",CreateUser.as_view()),
  path("logIn",logIn.as_view()),
  path("logOut",logOut.as_view()),
  path("jwt-login",JWTLogIn.as_view()),
]