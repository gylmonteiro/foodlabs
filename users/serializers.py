from rest_framework import serializers
from addresses.serializers import AddressSerializer
from users.models import User
from addresses.models import Address
class UserSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)

    address = AddressSerializer()


    def create(self, validated_data):
        address_data = validated_data.pop("address")
        
        user = User.objects.create(**validated_data)
        address = Address.objects.create(**address_data, user= user)
        return (user)