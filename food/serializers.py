from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from .models import Food, Order
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'discriptions',
            'day',
            'pic',
            'price',
            )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('food','user')

class OrderCancelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('food','user','reason','cancelled')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','email')
