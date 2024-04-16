from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad
from .serializers import AdSerializer



class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdListApiView(generics.ListAPIView):
    """ Ads list """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ad.objects.filter(author=user)


class AdCreateApiView(generics.CreateAPIView):
    """ creating an ad """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    pass
