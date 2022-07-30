from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from addresses.models import Address
from addresses.serializers import AddressSerializer
# Create your views here.

class AddressView(APIView):
    def get(self, _):
        addresses = Address.objects.all()
        list_addresses = AddressSerializer(addresses, many=True)
        return Response(list_addresses.data)
    
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)