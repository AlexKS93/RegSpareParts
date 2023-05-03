from api.serializers import SparePartSerializer
from reg.models import SpareParts
from rest_framework import (decorators, filters, permissions, response,
                            serializers, status, viewsets)


from django.shortcuts import render

class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartSerializer
    # permission_classes = (ReadOnly,)
    # filter_backends = [DjangoFilterBackend]
    # filter_class = IngredientsFilter

    # lookup_field = 'id'
    # pagination_class = None

