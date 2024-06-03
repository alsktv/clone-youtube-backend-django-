from rest_framework import serializers
from .models import Comment
from users.serializers import CommentUserSerializer
from videos.serializers import videoSerializer
from dirrerence_time import TimeDifference

class CommentSerializer(serializers.ModelSerializer):

  user = CommentUserSerializer(read_only = True)  #read_only를 해 줌으로써 유저가 입력하는 것을 방지함.
  content = videoSerializer(read_only = True)

  time_difference = serializers.SerializerMethodField()
  
  def get_time_difference(self,comment):
    return TimeDifference(comment.created_at)
  class Meta:
    model = Comment
    fields = ["user","text","content","time_difference"]