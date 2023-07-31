from django.shortcuts import render
from django.http import JsonResponse
from reg.models import SpareParts
from users.models import User
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import (decorators, filters, permissions, response,
                            serializers, status, viewsets)
from api.serializers import UserSerializer
# Create your views here.


def get_fields_list(request):
    fields_verbose_name = []
    fields_name = []
    #print(SpareParts._meta.get_fields())
    for field in SpareParts._meta.fields:
        #if 'verbose_name' in enumerate(dir(field)):
            #if 
        fields_verbose_name.append(field.verbose_name)
    #fields_verbose_name = [field.verbose_name for field in SpareParts._meta.get_fields()]
    for field in SpareParts._meta.fields:
        #SpareParts._meta.fields[0].verbose_name
        #if 'name' in dir(field):
        fields_name.append(field.name)
    #fields_name = [field.name for field in SpareParts._meta.get_fields()]
    fields_list = dict(zip(fields_name, fields_verbose_name))
    print(fields_list)
    output_field = []
    for index, item in enumerate(fields_list.keys()):
        if index == 0:
            output_field.append({'title': 'status',
                                 'field': 'status',
                                 'checkbox': 'true'})
            continue
        # if index == 1:
        #     continue
        output_field.append({'title': fields_list[item],
                             'field': item,
                             'sortable': 'true'})
    return JsonResponse(output_field[:-3], safe=False)


class UserViewSet(DjoserUserViewSet, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.DjangoModelPermissions,)
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('id',)
    lookup_field = 'id'
    #pagination_class = LimitPageNumberPagination

    # @decorators.action(
    #     methods=['GET', 'POST', 'DELETE'],
    #     detail=True,
    #     permission_classes=(permissions.IsAuthenticated,))
    # def subscribe(self, request, id):
    #     obj = get_object_or_404(self.queryset, id=id)
    #     serializer = UserSubscribeSerializer(obj)
    #     follow_obj = Follow.objects.filter(Q(author__id=id) &
    #                                        Q(user=request.user))
    #     if ((request.method in ['POST']) and
    #        not follow_obj):
    #         Follow(None, request.user.id, obj.id).save()
    #         return response.Response(serializer.data,
    #                                  status=status.HTTP_201_CREATED)

    #     if ((request.method in ['DELETE']) and
    #        follow_obj):
    #         follow_obj[0].delete()
    #         return response.Response(status=status.HTTP_204_NO_CONTENT)
    #     return response.Response(status=status.HTTP_400_BAD_REQUEST)

    # @decorators.action(
    #         methods=['get', ],
    #         detail=False)
    # def subscriptions(self, request):
    #     try:
    #         if not self.request.user.is_authenticated:
    #             return response.Response(status=status.HTTP_401_UNAUTHORIZED)

    #         pages = self.paginate_queryset(
    #             User.objects.filter(following__user=self.request.user)
    #         )
    #         serializer = UserSubscribeSerializer(pages, many=True)
    #         recipe_limit = request.query_params['recipe_limit']
    #         if recipe_limit:
    #             for data in serializer.data:
    #                 data['recipes'] = data['recipes'][:int(recipe_limit)]
    #         return self.get_paginated_response(serializer.data)
    #     except KeyError:
    #         return self.get_paginated_response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     user = User.objects.get(username=serializer.instance.username)
    #     password = request.data['password']
    #     user.set_password(password)
    #     user.save()
    #     return response.Response(serializer.data, status.HTTP_200_OK)