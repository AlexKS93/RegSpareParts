from django.urls import include, path
from reg.views import SparePartsViewSet
from rest_framework import routers



router = routers.DefaultRouter()


router.register(r'spareparts',
                SparePartsViewSet,
                basename="spareparts"
                )
# router.register(r'ingredients',
#                 IngredientsViewSet,
#                 basename="ingredients")
# router.register(r'recipes',
#                 RecieptsViewSet,
#                 basename="recipes")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
