from django.shortcuts import render
from django.http import JsonResponse
from reg.models import SpareParts
# Create your views here.


def get_fields_list(request):
    fields_verbose_name = [field.verbose_name for field in SpareParts._meta.get_fields()]
    fields_name = [field.name for field in SpareParts._meta.get_fields()]
    fields_list = dict(zip(fields_name, fields_verbose_name))
    print(fields_list)

    return JsonResponse([{'title': 'state', 'field': 'state',}], safe=False)#fields_list)
