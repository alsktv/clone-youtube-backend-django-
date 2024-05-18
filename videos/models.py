from django.db import models
from commonmodel.models import CommonModel

class Video(CommonModel):
  """ 
      video = 영상 url을 담음
      name = 영상 제목
      user = user
      categories = 영상 카테고리
      description = 영상 틀었을 때 밑에 더보기에 나오는 설명
  """
  video = models.CharField(max_length=500)
  name = models.CharField(max_length=100,default="")
  user = models.ForeignKey("users.User",on_delete=models.CASCADE, related_name = "video_user")
  categories = models.ManyToManyField("categories.Category")
  description = models.TextField(null = True, blank = True)
  #view_count = 
  #like_count = 
  #review = 

  def review_count(self):
    video = Video.objects.get(pk = self.pk)
    return video.reviews.count()


  def like_count(self):   # 좋아요 수
    video = Video.objects.get(pk = self.pk)
    return video.user_likeVideo.count()
  
  

  def __str__(self):
    return self.name
