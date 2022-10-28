from rest_framework import serializers

from food.models import FoodCategory


class FoodCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = (
          "__all__"
        )


# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodModel
#         fields = (
#           "__all__"
#         )

