from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = (
    "__str__",
    "email",
    "subscribe_count",
  )
  fieldsets = (
    ("user" , {"fields" : ("name","image","email","subscribe","likeVideo")}),
  )
  # def subscribe_count(self,users):
  #   user  = User.objects.get(pk = users.pk)
  #   return user.user_subscribe.all().count()  #reverse 변수로 가져온 것은 orm이여서 all()을 사용해야 queryset이 됨. 그런 다음에 count method를 작동시켜야함.
  
  def my_video(self,users):
    user  = User.objects.get(pk = users.pk)
    return user.video_user.all()
  
  