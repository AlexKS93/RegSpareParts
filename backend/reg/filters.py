from django_filters.rest_framework import CharFilter, FilterSet, filters

from reg.models import Categoryes


# class RecieptsFilter(FilterSet):
#     tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
#     is_favorited = (filters
#                     .BooleanFilter(method='filter_is_favorited'))
#     is_in_shopping_cart = (filters
#                            .BooleanFilter(method='filter_is_in_shopping_cart'))

#     class Meta:
#         model = Recipes
#         fields = ('author', 'tags', 'is_favorited', 'is_in_shopping_cart')

#     def filter_is_favorited(self, queryset, name, value):
#         return self.__get_for_filter_data(queryset, name, value)

#     def filter_is_in_shopping_cart(self, queryset, name, value):
#         return self.__get_for_filter_data(queryset, name, value)

#     def __get_for_filter_data(self, queryset, name, value):
#         if value and self.request and self.request.user.is_authenticated:
#             if name == 'is_in_shopping_cart':
#                 return (queryset
#                         .filter(reciept_in_shoplist__user=(self
#                                                            .request
#                                                            .user)))
#             if name == 'is_favorited':
#                 return (queryset
#                         .filter(reciept_favorits__user=(self
#                                                         .request
#                                                         .user)))
#         return queryset


class CategoryesFilter(FilterSet):
    name = CharFilter(
        field_name='name', lookup_expr='icontains'
    )

    class Meta:
        model = Categoryes
        fields = []
