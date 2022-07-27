from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=50)
    number = serializers.CharField()
    complement =  serializers.CharField(max_length=40, read_only=True)
