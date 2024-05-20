from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer
class Photos(APIView):
  def get(self,request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos , many = True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer = PhotoSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(PhotoSerializer(created_data).data)
    else: 
      return Response(serializer.errors)
    
    