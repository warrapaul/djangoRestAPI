from methodBased.models import Buildings
from methodBased.serializers import BuildingsModalSerializer,BuildingSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
  
   
   
 #List all code buildings, or create a new building.
@api_view(['GET', 'POST'])
def building_list(request, format=None):
    if request.method == 'GET':
        buildings = Buildings.objects.all()
        serializer = BuildingsModalSerializer(buildings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BuildingsModalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
#Retrieve, update or delete a code building.
@api_view(['GET', 'PUT', 'DELETE'])
def building_detail(request, pk, format=None):
 
    try:
        building = Buildings.objects.get(pk=pk)
    except Buildings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BuildingsModalSerializer(building)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BuildingsModalSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)