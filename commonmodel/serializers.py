from rest_framework.serializers import ModelSerializer
from users.models import User

class TinyUserSerializer(ModelSerializer):

  """vidoeDetail에서 사용함"""
  class Meta:
    model = User
    fields = ["name","image","subscribe_count"]