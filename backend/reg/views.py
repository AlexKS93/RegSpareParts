from api.serializers import (CategoryesSerializer,
                             SparePartSerializer,
                             ManufacturersSerializer,
                             SparePartPOSTSerializer)
from reg.filters import CategoryesFilter
from reg.models import Categoryes, SpareParts, Manufacturers, CategoryesEvents, SparePartsEvents
from users.models import User
from users.models import User
from rest_framework import (decorators, filters, permissions, response,
                            serializers, status, viewsets)

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render




class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartSerializer

    def perform_create(self, serializer):
        if SpareParts.objects.filter(**serializer.validated_data).exists():
            return response.Response({**serializer.validated_data}, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        rec = SpareParts.objects.get(**serializer.validated_data)
        create_event(self.request,
                        'POST',
                        SparePartsEvents,
                        serializer.validated_data,
                        rec)
    # def create(self, serializer):
    #     serializer = self.get_serializer(data=self.request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     user = User.objects.get(username=serializer.instance.username)
    #     password = self.request.data['password']
    #     user.set_password(password)
    #     user.save()
    #     return response.Response(serializer.data, status.HTTP_200_OK)

    # def get_serializer_class(self, *args, **kwargs):
    #     if self.request.method == 'GET':
    #         return SparePartSerializer
    #     return SparePartPOSTSerializer


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
    pagination_class = None


def create_event(request, event_type, object, data, rec):
    print(request.user)
    user = User.objects.get(username=request.user.username)
    object.objects.create(
        event_type=event_type,
        message="Создана запись",
        id_record=rec,
        user=user,
        data={**data}
    )


def index(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')
