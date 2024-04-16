from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """creating user"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ list of users """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ list of user """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ updating for user """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """ deleting a user """
    serializer_class = UserSerializer
    queryset = User.objects.all()
