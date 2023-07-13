from api.serializers import (CategoryesSerializer,
                             SparePartSerializer,
                             ManufacturersSerializer)
from reg.filters import CategoryesFilter
from reg.models import Categoryes, SpareParts, Manufacturers, CategoryesEvents, SparePartsEvents
from rest_framework import (decorators, filters, permissions, response,
                            serializers, status, viewsets)

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render


class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartSerializer

    def perform_create(self, serializer):
        serializer.save()
        rec = SpareParts.objects.get(**serializer.validated_data)
        create_event(self.request,
                        'POST',
                        SparePartsEvents,
                        serializer.validated_data,
                        rec)


class CategoryesViewSet(viewsets.ModelViewSet):
    queryset = Categoryes.objects.all()
    serializer_class = CategoryesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CategoryesFilter
    lookup_field = 'id'
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save()
        rec = Categoryes.objects.get(**serializer.validated_data)
        create_event(self.request,
                     'POST',
                     CategoryesEvents,
                     serializer.validated_data,
                     rec)


class ManufacturersViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturersSerializer


def create_event(request, event_type, object, data, rec):
    object.objects.create(
        event_type=event_type,
        message="Создана запись",
        id_record=rec,
        user=request.user,
        data={**data}
    )


def index(request):
    return render(request, 'main.html')
