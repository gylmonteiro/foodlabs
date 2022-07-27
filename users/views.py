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