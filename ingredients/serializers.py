from rest_framework import serializers
from ingredients.models import Ingredient
class IngredientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=40)

    # recipes = serializers.ManyToManyField("recipes.Recipe", related_name="ingredients")    

    def create(self, validated_data):
        ingredient = Ingredient.objects.create(**validated_data)
        return (ingredient)