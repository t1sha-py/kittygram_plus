from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from cats.views import CatViewSet, OwnerViewSet, LigthCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LigthCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
