from django.shortcuts import render
from .models import (
   Food,
   Order
)
from django.contrib.auth.models import User
from .serializers import (
    FoodSerializer, 
    OrderSerializer,
    OrderCancelSerializer,
    UserSerializer
    
)
from rest_framework import viewsets , serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

from django.views.generic import View


class FoodViewSet(viewsets.ModelViewSet):
    """
    A view that returns the count of active users in JSON.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name','day')

class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('food','user')


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            username = self.request.user.username
            user = User.objects.filter(username=username)
            return user
        
        except User.DoesNotExist:
            return User()

   
