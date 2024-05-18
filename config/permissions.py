import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication #이게 authentication class에서 상속받아야 하는 라이브러리임.
from rest_framework.exceptions import ValidationError
from users.models import User


class JWTAuthentication(BaseAuthentication):

  def authenticate(self, request): #request에 headers정보 있음을 기역하자!!!
    token = request.headers.get("authorization")
    if not token:
      raise ValidationError("don't make token")
    decode = jwt.decode(token,settings.SECRET_KEY, algorithms="HS256")
    pk = decode.get("pk")
    user = User.objects.get(pk = pk)
    if not user:
      raise ValidationError("user does not exist.")
    else:
      return (user,None)
