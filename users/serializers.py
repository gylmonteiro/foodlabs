from rest_framework import serializers
from addresses.serializers import AddressSerializer
class UserSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=100)

    address = AddressSerializer(read_only=True)