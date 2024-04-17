from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad, Comment
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


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

    def perform_create(self, serializer):
        # Setting the current user as the post author
        serializer.save(author=self.request.user)


class AdRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one ad """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsAdmin]


class AdUpdateApiView(generics.UpdateAPIView):
    """ updating an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class AdDestroyApiView(generics.DestroyAPIView):
    """ deleting an ad """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class CommentListApiView(generics.ListAPIView):
    """ comments list """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]


class CommentCreateApiView(generics.CreateAPIView):
    """ creating a comment """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Setting the current user as the post author
        serializer.save(author=self.request.user)


class CommentUpdateApiView(generics.UpdateAPIView):
    """ updating an ad """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class CommentDestroyApiView(generics.DestroyAPIView):
    """ deleting an ad """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwner | IsAdmin]
