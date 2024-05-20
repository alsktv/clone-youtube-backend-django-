from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import HTTP_200_OK
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

class CategoryDetail(APIView):
  permission_classes = [IsAuthenticated]
  def get_objects(self,pk):
    try:
      return Category.objects.get(pk= pk)
    except Category.DoesNotExist:
      raise ParseError("Does not exist")
  
  def get(self,request,pk):
    category = self.get_objects(pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
  
  def delete(self,request,pk):
   category = self.get_objects(pk)
   category.delete()
   return Response(status= HTTP_200_OK)
   

 


