from django.contrib import admin

from reg.models import Categoryes, Manufacturers, SpareParts, CategoryesEvents, SparePartsEvents

admin.site.register(Categoryes)
admin.site.register(Manufacturers)
admin.site.register(SpareParts)
admin.site.register(CategoryesEvents)
admin.site.register(SparePartsEvents)
