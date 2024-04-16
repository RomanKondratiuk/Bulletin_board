from rest_framework import pagination, viewsets, generics
from .models import Ad
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


class AdRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one ad """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


class AdUpdateApiView(generics.UpdateAPIView):
    """ updating an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdDestroyApiView(generics.DestroyAPIView):
    """ deleting an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    pass
