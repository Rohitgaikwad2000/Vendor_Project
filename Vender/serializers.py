from rest_framework import serializers
from .models import Vender, Purchase, Historical


class Venderserialiazer(serializers.ModelSerializer):
    class Meta:
        model = Vender
        fields = "__all__"


class Purchaseserialiser(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class Historicalserialiser(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = "__all__"
