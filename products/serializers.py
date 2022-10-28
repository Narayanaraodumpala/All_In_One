from rest_framework import serializers

from products.models import Cloths


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloths
        fields = (
          "__all__"
        )
