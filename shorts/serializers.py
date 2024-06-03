from rest_framework import serializers
from .models import Shorts
from categories.models import Category
from commonmodel.serializers import TinyUserSerializer
from django.utils import timezone
from categories.serializers import CategorySerializer


class ShortSerializer(serializers.ModelSerializer):

  user = TinyUserSerializer(read_only = True)

  time_difference = serializers.SerializerMethodField()

  categories = CategorySerializer()

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
    model = Shorts
    fields = ["pk","user","name","video","view_count", "time_difference","categories","review_count"]