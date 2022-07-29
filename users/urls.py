from django.urls import path
from users.views import UserView, UserViewDetails


urlpatterns = [

    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserViewDetails.as_view())

]