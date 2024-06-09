from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated,NotFound
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from .models import Video
from comments.models import Comment
from .serializers import videoSerializer,videoDetailSerializer
from comments.serializers import CommentSerializer
from django.conf import settings
from django.db.models import Q

class Videos(APIView):
  def get(self,request):
     videos = Video.objects.all()
     serializer = videoSerializer(videos, many = True)
     return  Response(serializer.data)
  
  def post(self,request):
      serializer = videoSerializer(data = request.data )
      updated = serializer.save()
      return Response(videoSerializer(updated).data)
  


class VideoDetail(APIView):
  permissions_classes = [IsAuthenticated]
  def get_object(self,pk):   #특정 비디오를 가져옴
     try:
      return Video.objects.get(pk = pk)
     except Video.DoesNotExist:
        raise NotFound

  def get(self,request,pk):
    serializer = videoDetailSerializer(self.get_object(pk))
    return Response(serializer.data)
  
  def put(self,request,pk):
     video = self.get_object(pk)
     view_count_state = request.data["view_count"] #영상 접속 시 plus라는 문자열을 받음
    # print(view_count_state)
     if(view_count_state == "plus"):
        new_view_count = video.view_count +1
        serializer = videoDetailSerializer(video, data = {"view_count":new_view_count})

        
     if serializer.is_valid():
      print("wwww")
      updated = serializer.save()
      return Response(videoDetailSerializer(updated).data)
     else:
        return Response(serializer.errors)
     
  def delete(self,request,pk):
     video = self.get_objects(pk)
     video.delete()
     return Response(status = HTTP_204_NO_CONTENT)
  


class Reviews(APIView):
   permissions_classes = [IsAuthenticated]
   def get_objects(self,pk):
         try:
            return Video.objects.get(pk = pk)
         except Video.DoesNotExist:
            raise NotFound
   def get(self,request,pk):

         page = int(request.query_params.get("page",1))
         reviews = self.get_objects(pk).reviews.all()
         serializer = CommentSerializer(reviews,many = True)
         print(serializer.data)
         return Response(serializer.data[(page-1)*settings.PAGE_WIDTH : page * settings.PAGE_WIDTH])
  

   def post(self,request,pk):
        user = request.user
        
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
         created_data = serializer.save(user = user , content = self.get_objects(pk))
         return Response(CommentSerializer(created_data).data)
        else:
          return Response(serializer.errors)

class searchVideo(APIView):  #검색창의 get요청을 처리하는 함수
   def get(self,request): 
      query = request.query_params.get("search_query" , "")  
      if query:
         search = Video.objects.filter(Q(name__icontains=query) | Q(user__name__icontains=query))
         serializer = videoSerializer(search , many = True)
         return Response(serializer.data)
      else:
         return Response(status=HTTP_204_NO_CONTENT)
 