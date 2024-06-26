import strawberry
from . import models
from strawberry import auto

@strawberry.django.type(models.User)
class UserType:
  name:auto
  email:auto
  likeVideo:auto

  