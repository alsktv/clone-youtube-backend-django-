from rest_framework import serializers
from .models import Video
from categories.models import Category
from commonmodel.serializers import TinyUserSerializer,UserInVidoeDetial
from django.utils import timezone
from categories.serializers import CategorySerializer
from dirrerence_time import TimeDifference

class videoSerializer(serializers.ModelSerializer):

  class CategorySerializer(serializers.ModelSerializer):
    class Meta:
      model = Category
      fields = ["name",]
    
  user = UserInVidoeDetial(read_only = True)

  time_difference = serializers.SerializerMethodField()

  categories = CategorySerializer()

  def get_time_difference(self,video):
   return TimeDifference(video.created_at)
       
  class Meta:
    model = Video
    fields = ["pk","user","name","video","view_count", "time_difference","categories"]

class videoDetailSerializer(serializers.ModelSerializer):

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
          model = Category
          fields = ["name"]
    
    categories = CategorySerializer(read_only = True)
  
    #댓글 수 나타냄
    review_count = serializers.SerializerMethodField()

    def get_review_count(self,video):
       return video.reviews.count()
    
    #좋아요 수 나타냄
    like_count = serializers.SerializerMethodField()

    def get_like_count(self,video):
       return video.user_likeVideo.count()
    
    user = UserInVidoeDetial(read_only = True)

    time_difference = serializers.SerializerMethodField()

    def get_time_difference(self,video):
      created_at = video.created_at
      now = now = timezone.now()
      time = (now - created_at).total_seconds() #시간 차이   #초단위로 나옴, 필요에 따라 변형해주기.
      if(time/60 < 60):
         return  f"{int(time//60)}분전"
      elif(time/3600 < 24):
         return  f"{int(time//3600)}시간전"
      elif((time/3600) // 24 < 30):
         return f"{int((time//3600)//24 )}일전"
      elif((time//3600)//24//30 < 12):
         return  f"{int((time//3600)//24//30 )}달전"
      else:
         return  f"{int((time//3600)//24//30//12) }년전"
   
    class Meta:
        model = Video
        fields =("pk", "user","name","view_count","like_count","review_count","categories","time_difference","video","description")


class alertVideoSerializer(serializers.ModelSerializer):
   
   class Meta:
    model = Video
    fields = ["name"]