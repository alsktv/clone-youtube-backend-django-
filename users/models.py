from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  name = models.CharField(max_length=20 ,default = "")
  email = models.CharField(max_length=30 , null=True , blank = True)
  image = models.URLField( null=True , blank = True)
  subscribe = models.ManyToManyField("users.User" , related_name="user_subscribe")
  likeVideo = models.ManyToManyField("videos.Video", related_name="user_likeVideo")
  alert = models.ManyToManyField("videos.Video", related_name="user_alert")
  likeComment = models.ManyToManyField("comments.Comment",null = True , blank = True , related_name = "comment_like")

  def subscribe_count(self):
    user  = User.objects.get(pk = self.pk)
    return user.user_subscribe.all().count()  #reverse 변수로 가져온 것은 orm이여서 all()을 사용해야 queryset이 됨. 그런 다음에 count method를 작동시켜야함.
  
  def __str__(self):
    return self.name

  
 