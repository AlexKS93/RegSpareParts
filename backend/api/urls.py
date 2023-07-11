from django.urls import include, path
from api.views import get_fields_list
from reg.views import CategoryesViewSet, SparePartsViewSet, ManufacturersViewSet
from rest_framework import routers



router = routers.DefaultRouter()


router.register(r'spareparts',
                SparePartsViewSet,
                basename="spareparts"
                )
router.register(r'categoryes',
                CategoryesViewSet,
                basename="categoryes")
router.register(r'manufacturers',
                ManufacturersViewSet,
                basename="manufacturers")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('get_fields_list/', get_fields_list)
]
