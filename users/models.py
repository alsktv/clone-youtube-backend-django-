from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  name = models.CharField(max_length=20 ,default = "")
  email = models.CharField(max_length=30 , null=True , blank = True)
  image = models.ImageField(null=True , blank=True)
  subscribe = models.ManyToManyField("users.User" , related_name="user_subscribe", blank=True)
  likeVideo = models.ManyToManyField("videos.Video", related_name="user_likeVideo" , blank=True)
  alert = models.ManyToManyField("users.User", related_name="user_alert" , blank=True)
  likeComment = models.ManyToManyField("comments.Comment" , blank = True , related_name = "comment_like")
  recent_video1 = models.ForeignKey ("videos.Video",on_delete=models.SET_NULL , null = True , blank = True ,related_name="user_recent_video1")
  recent_video2 = models.ForeignKey("videos.Video",on_delete=models.SET_NULL , null = True , blank = True, related_name="user_recent_video2")
  recent_video3 = models.ForeignKey("videos.Video",on_delete=models.SET_NULL , null = True , blank = True, related_name="user_recent_video3")
  recent_video4 = models.ForeignKey("videos.Video",on_delete=models.SET_NULL , null = True , blank = True, related_name="user_recent_video4")
  recent_video5 = models.ForeignKey("videos.Video",on_delete=models.SET_NULL , null = True , blank = True, related_name="user_recent_video5")

  def videos(self):
    from commonmodel.serializers import VideoInCommonSerializer
    user  = User.objects.get(pk = self.pk)
    serializer = VideoInCommonSerializer(user.video_user , many = True)
    return serializer.data

  def subscribe_count(self):
    user  = User.objects.get(pk = self.pk)
    return user.user_subscribe.all().count()  #reverse 변수로 가져온 것은 orm이여서 all()을 사용해야 queryset이 됨. 그런 다음에 count method를 작동시켜야함.
  
  
  def __str__(self):
    return self.name

  
 