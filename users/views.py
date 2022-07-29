from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from users.models import User
from users.serializers import UserSerializer
# Create your views here.
class UserView(APIView):
    def get(self, _):
        users = User.objects.all()
        list_users_serializer = UserSerializer(users, many=True)
        return Response(list_users_serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        # if serializer.is_valid():
        #     user = User.objects.create(**serializer.validate_data)
        #     user.save()
        #     return Response(serializer.data)
        # else:
        #     errors = serializer.errors
        #     return Response(errors)
        serializer.is_valid(raise_exception=True)

        # user = User(**serializer.validated_data)
        # user.save()
        # serializer_out = UserSerializer(user)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserViewDetails(APIView):
    def get(self, request, user_id):

        # try:
        #     user =  User.objects.get(pk=user_id)
        # except User.DoesNotExist:
        #     return Response({"error": "Usuário não existe"}, status.HTTP_404_NOT_FOUND)
        # user_serializer = UserSerializer(user)
        # return Response(user_serializer.data, status.HTTP_200_OK)

        user = get_object_or_404(User, pk=user_id)
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data)

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

    def patch(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user_serializer = UserSerializer(user, request.data, partial= True )
        user_serializer.is_valid(raise_exception=True)

        try:
            user_serializer.save()
        except KeyError:
            return Response({"errors": "não pode atualizar o endereço"}, status.HTTP_400_BAD_REQUEST)

        return Response(user_serializer.data)


