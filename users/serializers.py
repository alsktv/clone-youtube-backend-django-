from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from commonmodel.serializers import TinyUserSerializer
from videos.serializers import videoSerializer


class CommentUserSerializer(ModelSerializer):

  """reviews에서 사용"""

  class Meta:
    model = User
    fields = ["name","image",]

class UserDetailSerialzer(ModelSerializer):

  subscribe_count = serializers.SerializerMethodField()
  likeVideo = videoSerializer(many = True,read_only = True)
  subscribe = TinyUserSerializer(read_only = True , many = True) #many = True 안넣으면 null 출력됨


  def get_subscribe_count(self,user):
    return user.user_subscribe.all().count()
  
  class Meta:
    model = User
    exclude = ["id",
               "password",
               "first_name",
               "last_name",
               ]