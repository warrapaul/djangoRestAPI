from methodBased.models import Buildings
from methodBased.serializers import BuildingsModalSerializer,BuildingSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
  
   
   
 #List all code buildings, or create a new building.
class building_list(APIView):
    def get (self, request):
        buildings = Buildings.objects.all()
        serializer = BuildingsModalSerializer(buildings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuildingsModalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
#Retrieve, update or delete a code building.
class building_detail(APIView):
    def get_object(self, pk):

        try:
            return Buildings.objects.get(pk=pk)
        except Buildings.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        building = self.get_object(pk)
        serializer = BuildingsModalSerializer(building)
        return Response(serializer.data)

    def put(self, request, pk):
        building = self.get_object(pk)
        serializer = BuildingsModalSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        building = self.get_object(pk)
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)