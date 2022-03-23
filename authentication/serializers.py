from authentication.models import Buildings
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    buildings = serializers.PrimaryKeyRelatedField(many=True, queryset=Buildings.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id','username','buildings','owner']


        
class BuildingsModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = ['region','zone','buildingName','buildingCode','mtrNo','token','buildingCode','revenue']


