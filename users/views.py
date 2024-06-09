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
from rest_framework.status import HTTP_400_BAD_REQUEST
from videos.models import Video
from django.db.models import Case, When,  F, Value, CharField
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

  def put(self,request,pk):
   
    user = self.get_objects(pk)
    subscribePk =  request.data.get("subscribe") #리스트

    recent_videoPk = request.data.get("recent_video") #리스트

    if(subscribePk):
      
      for index in subscribePk:
        try:
          Test = User.objects.get(pk = index)
        except User.DoesNotExist:
          raise ParseError("Pk does not exist")
      is_subscribed = any(sub.pk in subscribePk for sub in user.subscribe.all()) 

      if(is_subscribed):
        subscribes = user.subscribe.all().exclude(pk__in = subscribePk)
      else:
        subscribe = User.objects.filter(pk__in = subscribePk)
        subscribes =  user.subscribe.all() | subscribe

    #recent_videos 에 관한 put요청 처리

    if(recent_videoPk):
      # print(recent_videoPk)
      old_video1 = user.recent_video1
      old_video2 = user.recent_video2
      old_video3 = user.recent_video3
      old_video4 = user.recent_video4
      old_video5 = user.recent_video5
      old_list = [old_video1 , old_video2 , old_video3 , old_video4 , old_video5]

      len = 1

      for x in old_list:
        if x == None:
         break
        len += 1

      print(len)
      
      if len<5 :
        
        for i in range(len):
          
          old_list[(len)-i] = old_list[(len-1)-i]
        old_list[0] = Video.objects.get(pk = recent_videoPk[0])
        print(old_list)
      else:
        for i in range(4):
          old_list[4-i] = old_list[3-i]
        old_list[0] = Video.objects.get(pk = recent_videoPk[0])



    serializer = UserDetailSerialzer(user , data=request.data , partial = True)

    if serializer.is_valid():
      
      
      if(recent_videoPk):
        updated_data = serializer.save(recent_video1 = old_list[0] ,
                                        recent_video2 = old_list[1] ,
                                        recent_video3 = old_list[2],
                                        recent_video4 = old_list[3],
                                        recent_video5= old_list[4])
      if(subscribePk):
        updated_data = serializer.save(subscribe = subscribes)
 
      return Response(UserDetailSerialzer(updated_data).data)
    else:
      return Response(serializer.errors)
  
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

  
