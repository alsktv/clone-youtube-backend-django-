from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Shorts
from .serializers import ShortSerializer


class shorts(APIView):

  permission_classes = [IsAuthenticated]

  def get(self,request):
    short = Shorts.objects.all()
    serializer = ShortSerializer(short, many = True)
    return Response(serializer.data)
  
  def post(self,request):
     
      serializer = ShortSerializer(data = request.data )
      updated = serializer.save()
      return Response(ShortSerializer(updated).data)
  
  

