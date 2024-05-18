from rest_framework.serializers import ModelSerializer
from .models import Comment
from users.serializers import CommentUserSerializer
from videos.serializers import videoSerializer

class CommentSerializer(ModelSerializer):

  user = CommentUserSerializer(read_only = True)  #read_only를 해 줌으로써 유저가 입력하는 것을 방지함.
  content = videoSerializer(read_only = True)


  class Meta:
    model = Comment
    fields = ["user","text","created_at","content"]