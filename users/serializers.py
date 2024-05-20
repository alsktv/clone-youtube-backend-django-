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

  subscribe_count = serializers.SerializerMethodField()
  likeVideo = videoSerializer(many = True,read_only = True)
  subscribe = TinyUserSerializer(read_only = True , many = True) #many = True 안넣으면 null 출력됨
  alert = AlertVideoSerializer(many = True)
  


  def get_subscribe_count(self,user):
    return user.user_subscribe.all().count()
  
  class Meta:
    model = User
    exclude = ["id",
               "password",
               "first_name",
               "last_name",
               ]
    

