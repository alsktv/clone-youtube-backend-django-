from .models import User

def get_user(pk:int):
  return User.objects.get(pk = pk)