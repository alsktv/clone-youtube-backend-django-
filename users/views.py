import jwt
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound,ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserDetailSerialzer
from django.http import JsonResponse
class UserDetail(APIView):
  permission_classes = [IsAuthenticated]
  
  def get_objects(self,pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise NotFound
 
  def get(self,request,pk):
    user = self.get_objects(pk)
    return Response(UserDetailSerialzer(user).data)
  
class CreateUser(APIView):
  def post(self,request):
    serializer = UserDetailSerialzer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(UserDetailSerialzer(created_data).data)
    else:
      return Response(serializer.errors)
    
class logIn(APIView):
  def post(self,request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
      return ParseError()
    user = authenticate(request,username = username , password = password)
    if user:
      login(request,user)
      return Response({"status":"ok"})
    else:
      return Response({"error":"wrong password"})
    
class logOut(APIView):
  permission_classes = [IsAuthenticated]

  def post(self,request):
    logout(request)
    return Response({"status" : "logout is succesful"})
  
class JWTLogIn(APIView):

  def post(self,request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
      raise ParseError("you must write username and password")
    user = authenticate(request, username= username, password = password)
    if user:
      token  = jwt.encode({"pk":user.pk}, settings.SECRET_KEY , algorithm="HS256" )
      return Response({"token": token})
    else:
          return Response({
           "error":"wrong password",
         })

  
