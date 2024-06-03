from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User
from videos.models import Video
from django.utils import timezone
from dirrerence_time import TimeDifference
class TinyUserSerializer(ModelSerializer):

  # def get_videos(self,user):
  #   video = user.video.user
  #   serializer = VideoInCommonSerializer (video , many = True)
  #   return serializer.data

  class Meta:
    model = User
    fields = ["pk","name","image","subscribe_count","videos"]

class VideoInCommonSerializer(ModelSerializer):

  time_difference = serializers.SerializerMethodField()

  def get_time_difference(self,video):
    return TimeDifference(video.created_at)

  class Meta:
    model = Video
    fields = ["user","name","video","view_count","time_difference"]

class UserInVidoeDetial(ModelSerializer):
    

  
  class Meta:
      model = User
      fields = ["pk","name","subscribe_count","image",]