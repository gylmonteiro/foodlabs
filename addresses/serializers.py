from rest_framework import serializers
from users.models import User
from addresses.models import Address

class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=50)
    number = serializers.CharField()
    complement =  serializers.CharField(max_length=40, read_only=True)
    