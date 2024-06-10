from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from commonmodel.serializers import TinyUserSerializer
from videos.serializers import videoSerializer, alertVideoSerializer



class CommentUserSerializer(ModelSerializer):

  """reviews에서 사용"""

  class Meta:
    model = User
    fields = ["name","image",]

class AlertVideoSerializer(ModelSerializer):

  video = serializers.SerializerMethodField()

  def get_video(self,user):
    videos = user.video_user
    serializer = alertVideoSerializer(videos, many = True)
    return serializer.data
  

  class Meta:
    model = User
    fields = ["name","image","video"]

class UserDetailSerialzer(ModelSerializer):

  subscribe_count = serializers.SerializerMethodField(read_only = True)
  likeVideo = videoSerializer(many = True)
  subscribe = TinyUserSerializer( many = True) #many = True 안넣으면 null 출력됨
  alert = AlertVideoSerializer(many = True)
  subscribe = TinyUserSerializer(read_only = True ,  many = True) #read_only는 유저가 입력하는 것을 무시하고 내가 값을 직접 입력하겠다는 뜻. 값을 커스텀 해서 집어넣어야 할때도 사용해야함.


  recent_video1 = videoSerializer(read_only = True)
  recent_video2 = videoSerializer(read_only = True)
  recent_video3 = videoSerializer(read_only = True)
  recent_video4 = videoSerializer(read_only = True)
  recent_video5 = videoSerializer(read_only = True)


  def get_subscribe_count(self,user):
    return user.user_subscribe.all().count()
  
  class Meta:
      model = User
      fields = [
        "pk",
        "likeVideo",
        "subscribe",
        "alert",
        "name",
        "email",
        "image",
        "subscribe_count",
        "recent_video1",
        "recent_video2",
        "recent_video3",
        "recent_video4",
        "recent_video5",
        "videos",
      ]


    
