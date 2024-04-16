from django.urls import path
from .apps import SalesConfig
from .views import AdListApiView, AdCreateApiView, AdRetrieveApiView,\
    AdUpdateApiView, AdDestroyApiView

# TODO настройка роутов для модели
app_name = SalesConfig.name


urlpatterns = [
    path('', AdListApiView.as_view(), name=' ad list'),
    path('ad/create/', AdCreateApiView.as_view(), name='ad-create'),
    path('ad/<int:pk>/', AdRetrieveApiView.as_view(),
         name='read one ad'),
    path('ad/update/<int:pk>/', AdUpdateApiView.as_view(),
         name='ad-update'),
    path('ad/delete/<int:pk>/', AdDestroyApiView.as_view(),
         name='ad-delete'),
]
