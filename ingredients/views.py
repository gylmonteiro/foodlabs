from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer

# Create your views here.
class IngredientsView(APIView):
    def get(self, _):
        ingredients = Ingredient.objects.all()
        ingredients_serializers = IngredientSerializer(ingredients, many=True)
        return Response(ingredients_serializers.data)
    
    def post(self,request):
        ingredient_serializer = IngredientSerializer(data=request.data)
        ingredient_serializer.is_valid(raise_exception=True)
        ingredient_serializer.save()
        return Response(ingredient_serializer.data, status.HTTP_201_CREATED)

class IngredientsDetails(APIView):
    def delete(self,_,ing_id):
        ingredient = get_object_or_404(Ingredient, pk=ing_id)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)