from django.urls import path
from ingredients.views import IngredientsView, IngredientsDetails


urlpatterns = [

    path("ingredients/", IngredientsView.as_view()),
    path("ingredients/<int:ing_id>/", IngredientsDetails.as_view()),

]