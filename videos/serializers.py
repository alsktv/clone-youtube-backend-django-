from rest_framework import serializers
from .models import Video
from categories.models import Category
from commonmodel.serializers import TinyUserSerializer

class videoSerializer(serializers.ModelSerializer):

  class CategorySerializer(serializers.ModelSerializer):
    class Meta:
      model = Category
      fields = ["name",]
    
  user = TinyUserSerializer(read_only = True)


  class Meta:
    model = Video
    fields = ["user","name","video","user",]

class videoDetailSerializer(serializers.ModelSerializer):

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
          model = Category
          fields = ["name"]
    
    categories = CategorySerializer()
  
    #댓글 수 나타냄
    review_count = serializers.SerializerMethodField()

    def get_review_count(self,video):
       return video.reviews.count()
    
    #좋아요 수 나타냄
    like_count = serializers.SerializerMethodField()

    def get_like_count(self,video):
       return video.user_likeVideo.count()
   
    class Meta:
        model = Video
        fields ="__all__"

