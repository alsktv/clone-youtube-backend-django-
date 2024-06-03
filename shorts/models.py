from django.db import models
from commonmodel.models import CommonModel

class Shorts(CommonModel):
  """ 
      video = 영상 url을 담음
      name = 영상 제목
      user = user
      categories = 영상 카테고리
      description = 영상 틀었을 때 밑에 더보기에 나오는 설명
  """
  video = models.URLField(max_length=500)
  name = models.CharField(max_length=100,default="")
  user = models.ForeignKey("users.User",on_delete=models.CASCADE, related_name = "short_user")
  categories = models.ForeignKey("categories.Category", null = True, on_delete=models.SET_NULL )
  description = models.TextField(null = True, blank = True)
  view_count =  models.IntegerField(default=0) #일딴은 숫자 넣어줌. 나중에 함수 구현하기
  #like_count = 
  #review = 

  def review_count(self):
    short = Shorts.objects.get(pk = self.pk)
    return short.reviews.count()


  def like_count(self):   # 좋아요 수
    short = Shorts.objects.get(pk = self.pk)
    return short.user_likeVideo.count()
  
  

  def __str__(self):
    return self.name

