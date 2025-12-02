from django.shortcuts import render
from rest_framework import viewsets

from user.models import User
from .serializers import UserCreateSerializer


# Create your views here.

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer