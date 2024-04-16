from django.urls import include, path
from .apps import SalesConfig
from .views import AdListApiView, AdCreateApiView

# TODO настройка роутов для модели
app_name = SalesConfig.name

urlpatterns = [
    path('', AdListApiView.as_view(), name=' ad list'),
    path('ad/create/', AdCreateApiView.as_view(), name='ad-create'),
    # path('habit/', HabitListApiView.as_view(), name='habit-list'),
    # path('habit/<int:pk>/', HabitRetrieveApiView.as_view(),
    #      name='read one habit'),
    # path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    # path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(),
    #      name='habit-update'),
    # path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(),
    #      name='habit-delete'),
]
