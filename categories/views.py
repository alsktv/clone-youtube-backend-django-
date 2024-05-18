from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class Categories(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer = CategorySerializer(date = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(CategorySerializer(created_data).data)
    else:
      serializer.errors()

 


