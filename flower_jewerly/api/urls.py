from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
