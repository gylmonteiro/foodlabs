from rest_framework import serializers
from addresses.serializers import AddressSerializer
from users.models import User
from addresses.models import Address
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name= serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)

    address = AddressSerializer()


    def create(self, validated_data):
        address_data = validated_data.pop("address")
        
        user = User.objects.create(**validated_data)
        Address.objects.create(**address_data, user= user)
        return (user)

    def update(self, instance: User, validated_data: dict):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        
        non_editable_keys = ("address",)
        if "address" in non_editable_keys:
            raise KeyError
        
        instance.save()

        return instance