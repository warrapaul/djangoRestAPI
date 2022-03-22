from methodBased.models import Buildings
from rest_framework import serializers


class BuildingsModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = ['region','zone','buildingName','buildingCode','mtrNo','token','buildingCode','revenue']



        

class BuildingSerializer(serializers.Serializer):
    region = serializers.CharField( max_length = 20)

    zone = serializers.CharField(max_length=30)
    buildingName = serializers.CharField(max_length=30)
    buildingCode = serializers.CharField(max_length=30)
    mtrNo = serializers.CharField(max_length=30)
    token = serializers.CharField(max_length=30)
    revenue = serializers.CharField(max_length=30)

    #create and return instance for validating data
    def create(self, validated_data):
         return Buildings.objects.create(**validated_data)

    #update and return exsiting instance
    def update(self, instance, validated_data):
        instance.region = validated_data.get('region' ,instance.region)
        instance.zone = validated_data.get('zone' ,instance.zone)
        instance.buildingName = validated_data.get('buildingName' ,instance.buildingName)
        instance.buildingCode = validated_data.get('buildingCode' ,instance.buildingCode)
        instance.mtrNo = validated_data.get('mtrNo' ,instance.mtrNo)
        instance.token = validated_data.get('token' ,instance.token)
        instance.revenue = validated_data.get('revenue' ,instance.revenue)

        instance.save()
        return instance

