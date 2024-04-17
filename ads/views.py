from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Ad, Comment
from .paginators import AdPagination
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdListApiView(generics.ListAPIView):
    """ Ads list """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_queryset(self):
        """
        search advertisements by name
        """
        queryset = self.queryset
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset


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
