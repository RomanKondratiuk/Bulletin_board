from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


class AdListApiView(generics.ListAPIView):
    """ Ads list """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdCreateApiView(generics.CreateAPIView):
    """ creating an ad """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one ad """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class AdUpdateApiView(generics.UpdateAPIView):
    """ updating an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsAdmin]


class AdDestroyApiView(generics.DestroyAPIView):
    """ deleting an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsAdmin]


class CommentViewSet(viewsets.ModelViewSet):
    pass
