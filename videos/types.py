import strawberry
from . import models
from strawberry import auto
from users.types import UserType

@strawberry.django.type(models.Video)   #django모델을 기준으로 type을 작성해 줌
class Video:
  id: auto
  name: auto
  user: "UserType"