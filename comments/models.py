from django.db import models
from commonmodel.models import CommonModel

class Comment(CommonModel):
  """ 댓글에 관한 클래스임
      user -> 유저 나타냄
      text -> 댓글의 내용 나타냄
      content -> 이 댓글이 달린 영상 나타냄
  """
  user = models.ForeignKey("users.User",on_delete=models.CASCADE)
  text = models.TextField()
  content_video = models.ForeignKey("videos.Video",on_delete=models.CASCADE, null = True,related_name="reviews")
  content_short = models.ForeignKey("shorts.Shorts",on_delete=models.CASCADE, null = True,related_name="reviews")
  review = models.ForeignKey("comments.Comment",on_delete=models.CASCADE, null = True , blank = True)
  
  def like_count(self):
    return self.comment_like.count()
  
  def __str__(self):
    return f"{self.user}:{self.text}"

