from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet


router = routers.DefaultRouter()

router.register(r'users',
                UserViewSet,
                basename="users")

urlpatterns = [
    path('', include(router.urls)),
]